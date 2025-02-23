from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'priority': forms.Select(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]),
            'status': forms.Select(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')]),
        }
