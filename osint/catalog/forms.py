from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


# class EntityForm(forms.ModelForm):
#     class Meta:
#         model = Entity
#         fields = '__all__'
#
# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Entity
#         fields = ('logo',)
