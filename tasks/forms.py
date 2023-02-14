from django import forms
from tasks.models import TaskModel

class Task_form(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'summary',
            'description',
            'completed',
            'assignee',
        ]

        # widgets = {
        #     'description': forms.TextInput()
        # }