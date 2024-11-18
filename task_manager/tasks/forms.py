from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class   Meta :
        model = Task
        fields = ['tache', 'description', 'status', 'date_echeance']
        widgets = {
            'tache': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la tâche'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date_echeance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }