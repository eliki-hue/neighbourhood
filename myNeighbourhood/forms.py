
from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,NeighbourHood, Business, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['username']
        fields ='__all__'

class NeighbourHodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        
        fields ='__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields='__all__'

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class PostForm(forms.ModelForm):
   
    class Meta:
        model:Post
        field = '__all__'