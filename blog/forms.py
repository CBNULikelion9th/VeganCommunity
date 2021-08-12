from django import forms
from django.db import models
from django.forms import fields
from .models import Post, Report, Add, Save

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = '__all__'


class SaveForm(forms.ModelForm):

    class Meta:
        model = Save
        fields = '__all__'

class AddForm(forms.ModelForm):

    class Meta:
        model = Add
        fields = 'add_content',