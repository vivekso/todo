from django.urls import path
from . import views
# from .views import delete_task, add_task


urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # New edit URL
]

