from django import forms
from .models import User
from django.core import validators

class UserMessage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'id':'w3lName', 'placeholder':'Name'}),
            'email': forms.TextInput(attrs={'id':'w3lSender', 'placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'id':'w3lName', 'placeholder':'Contact'}),
            'message': forms.Textarea(attrs={'id':'w3lMessage', 'placeholder':'Message*'}),
        }