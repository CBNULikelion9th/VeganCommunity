from django import forms
from .models import User, Post, Market_Post, Market_Comment

# login
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password', 'email', 'username', 'vegan', 'is_active',
                  'is_admin', 'is_superuser', 'is_staff') 

# user_custom store -> 이름 바꿔야 됨
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# market
class MarketPostForm(forms.ModelForm):
    class Meta:
        model = Market_Post
        fields = '__all__'

class MarketCommentForm(forms.ModelForm):
    class Meta:
        model = Market_Comment
        fields = '__all__'