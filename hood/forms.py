from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import Post,Neighborhood


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    
    class  Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


class newHoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name','location','profile_pic')
        
class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['content','image']