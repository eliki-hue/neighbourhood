from urllib import response
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NeighbourHodForm, PostForm, BusinessForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    neighbourHood = NeighbourHood.objects.all()
    message ="Select your Neighbourhoods"
    

    return render(request,'index.html',{'neighbourhood': neighbourHood, 'message': message})


