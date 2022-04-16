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

def add_business(request):
    if request.method =='POST':
        form = BusinessForm(request.Post)
        if form.is_valid():
            form.save()
    
    else:
        form = BusinessForm()

        return render(request, 'add_business.html', {'form':form})

def add_post(request):
    if request.method =='POST':
        form = BusinessForm(request.Post)
        if form.is_valid():
            form.save()
    
    else:
        form = BusinessForm()

        return render(request, 'add_post.html', {'form':form})

def add_neighbourhood(request):
    if request.method =='POST':
        form = NeighbourHodForm(request.Post)
        if form.is_valid():
            form.save()
    
    else:
        form = NeighbourHodForm()
        return render(request, 'add_neighbourhood.html', {'form':form})

def search_results(request):

    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        try:
            searched_result = NeighbourHood.search(search_term)
            message = f"Found searched project by title {search_term}"
        except NeighbourHood.DoesNotExist:
             message="No project with that title please try a different title."
             return render(request, 'NotFound.html',{'message':message})


        return render(request, 'search.html',{'message':message,"search_result": searched_result})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

