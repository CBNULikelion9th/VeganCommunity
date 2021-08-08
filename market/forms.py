from django import forms
from .models import Market_Post, Market_Comment


class PostForm(forms.ModelForm):
    class Meta: 
        model = Market_Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Market_Comment
        fields = '__all__'