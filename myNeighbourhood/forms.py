
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

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        
        fields ='__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields='__all__'


class PostForm(forms.ModelForm):
   
    class Meta:
        model=Post
        fields='__all__'