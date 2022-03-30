from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput
from .models import Post, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Заголовок"
            }),
            'content': Textarea(attrs={
                'placeholder': "Текст",
                "margin-top": "15px",
            }),

        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

