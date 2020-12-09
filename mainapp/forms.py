from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment...', 'rows':3, 'cols': 100}))
    class Meta:
        model = Comment
        fields = ('body',)