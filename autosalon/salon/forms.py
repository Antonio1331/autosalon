from django import forms
from .models import Car, Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'name', 'year', 'price', 'image', 'is_available']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
