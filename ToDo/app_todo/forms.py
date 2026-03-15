from app_todo.models import TODO
from django import forms
class NewTODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'description']