from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]

    # def save(self, data):
    #     print("data: ", data)
    #     return data


class LoginForm(forms.ModelForm):
    class Meta:
        username = forms.CharField(widget=forms.Textarea())
        model = User
        fields = [
            "username",
            "password"
        ]
