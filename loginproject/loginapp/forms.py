from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#회원 가입 폼
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

#회원 가입 폼2
class signform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()