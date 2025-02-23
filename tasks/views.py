from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm
import logging
from django.contrib import messages


logger = logging.getLogger(__name__)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            error = "Invalid username or password. Please try again."

    return render(request, 'tasks/login.html', {'error': error})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.soft_delete()  # Soft delete instead of deleting permanently
    return redirect('task_list')

def register_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            return render(request, 'tasks/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'tasks/register.html', {'error': 'Username already taken'})

        if User.objects.filter(email=email).exists():
            return render(request, 'tasks/register.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
        user.save()
        return redirect('login')

    return render(request, 'tasks/register.html')

def task_list(request):
    sort_by = request.GET.get('sort_by', 'due_date')  # Default sorting by due date
    order = request.GET.get('order', 'asc')

    sort_mapping = {
        'priority': 'priority',
        'due_date': 'due_date'
    }

    if sort_by in sort_mapping:
        order_prefix = '' if order == 'asc' else '-'
        tasks = Task.objects.filter(user=request.user, is_deleted=False).order_by(f"{order_prefix}{sort_mapping[sort_by]}")
    else:
        tasks = Task.objects.filter(user=request.user, is_deleted=False).order_by("due_date")

    form = TaskForm()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form, 'sort_by': sort_by, 'order': order})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        logger.debug(f"Received data: title={title}, description={description}, priority={priority}, due_date={due_date}, user={request.user}")

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to add tasks.")
            return redirect('login')

        if title and description and priority and due_date:
            try:
                task = Task.objects.create(
                    title=title,
                    description=description,
                    priority=priority,
                    due_date=due_date,
                    user=request.user
                )
                task.save()
                messages.success(request, "Task added successfully!")
                return redirect('task_list')
            except Exception as e:
                logger.error(f"Error while saving task: {e}")
                messages.error(request, "Failed to add task. Please try again.")

    # If GET request or task creation fails, show existing tasks
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user, is_deleted=False)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def logout_view(request):
    logout(request)
    return redirect('login')

