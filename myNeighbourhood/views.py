from email import message
from urllib import response
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, NeighbourHoodForm, PostForm, BusinessForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    neighbourHood = NeighbourHood.objects.all()
    message ="Select your Neighbourhoods"
    

    return render(request,'index.html',{'neighbourhoods': neighbourHood, 'message': message})


@login_required(login_url='/accounts/login/')
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile= Profile.objects.filter(username=current_user)
            print(profile)
            if profile:
                print('profile exist')
                username = current_user
                useremail=form.cleaned_data['useremail']
               
                userage=form.cleaned_data['userage']
                profile_image=form.cleaned_data['profile_image']
                AuthenticationError=form.cleaned_data['AuthenticationError']
                Profile.objects.filter(username=current_user).update(useremail=useremail, userage=userage,profile_image=profile_image,AuthenticationError=AuthenticationError)
            else:
                print('profile does not exist')
                profile=form.save(commit=False)
                profile.username= current_user
                profile.save()

            message='saved successfuly'
            # profile_display(request)
            return redirect(profile_display)
    
            
    else:
        form = ProfileForm()
        
    return render(request, 'profile.html',{'form':form})
       
       
@login_required(login_url='/accounts/login/')
def profile_display(request):

    current_user = request.user
    profile= Profile.objects.filter(username=current_user)
   

    return render(request, 'profiledisplay.html',{'profile':profile})

@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method =='POST':
        print('received')
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('saved successfully')
            return redirect(home)
        else:
            print('not not saved')
    
    else:
        print('get request')
        form = BusinessForm()
        return render(request, 'add_business.html', {'form':form})
    return redirect('home')

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method =='POST':
        
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
            print('post saved successfully')
    
    else:
        form = PostForm()

        return render(request, 'add_post.html', {'form':form})
    return redirect('single_neighbourhood')

@login_required(login_url='/accounts/login/')
def add_neighbourhood(request):
    if request.method =='POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    
    else:
        form = NeighbourHoodForm()
        return render(request, 'add_neighbourhood.html', {'form':form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        try:
            searched_result = Business.search_business(search_term)
            message = f"Found searched business {search_term}"
        
        except Business.DoesNotExist:
             message="No business with that name try a different name."
             return render(request, 'NotFound.html',{'message':message})


        return render(request, 'search.html',{'message':message,"search_result": searched_result})

    else:
        message = "You haven't searched for any Business"
        return render(request, 'search.html',{"message":message})

def single_neighbourhood(request, pk):
    
    print('searching....................')
    belonging=NeighbourHood.objects.get(id=pk)
    print(belonging)

    return render(request, 'home.html',{'neighbourhood':belonging})



