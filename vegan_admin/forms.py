from django import forms
from signup.models import User
from blog.models import Post, Report, Add
from market.models import Market_Post, Market_Comment

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

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
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