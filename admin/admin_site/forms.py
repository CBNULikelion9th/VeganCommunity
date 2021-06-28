from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class VeganStoreForm(forms.ModelForm):
    class Meta:
        model = Vegan_Store
        fields = '__all__'
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Store_Review
        fields = ('star', 'review')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class GoodForm(forms.ModelForm):
    class Meta:
        model = Market_Goods
        fields = '__all__'