from django import forms
from django.db import models
from django.forms import fields
from .models import Post, Report, Add

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = 'report_content',


class AddForm(forms.ModelForm):

    class Meta:
        model = Add
        fields = 'add_content',