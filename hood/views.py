from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from .forms import RegisterUserForm,newHoodForm, PostForm

from .models import Neighborhood, Post, Profile, HoodMember



# Landing page
def index(request):
    return render(request,'index.html')


# Dashboard to show neighborhoods
def dashboard(request):
    
    hoods = Neighborhood.objects.all()
    context = {
        'hoods':hoods
    }
    
    return render(request,'dashboard.html',context)

# Home posts and details
def home(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    hood_group = HoodMember.objects.filter(member=current_user).first()
    hood = hood_group.hood
    posts =''
    context = {
        'hood':hood,
        'posts':posts
    }
    return render(request,'home.html', context)

# Creating new Neighborhood
@login_required(login_url='/accounts/login')
def new_hood(request):
    if request.method == 'POST':
        current_user = request.user
        profile = Profile.objects.filter(user=current_user).first()
        form = newHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.creator = current_user
            hood.save()
            new_member = HoodMember(member=current_user,hood=hood)
            new_member.save()
            messages.success(request,('Neighborhood created!'))
            return redirect('dashboard')
    else:
        form = newHoodForm()
    return render(request,'new-hood.html', {'form':form})


# Joinin a neighborhood
@login_required(login_url='/accounts/login')
def join_hood(request,hood_id):
    hood = get_object_or_404(Neighborhood,id=hood_id)
    new_member = HoodMember(member = request.user, hood= hood)
    new_member.save()
    messages.success(request,("You've joined the group"))
    return redirect('home')

# Creating newpost
@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        current_user = request.user
        hood = current_user.Profile.neigborhood
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.hood = hood
            post.save()
            messages.success(request,('Posted!'))
        return HttpResponseRedirect(request.path_info)
           
    else:
        form = PostForm() 
    return render(request,'add_post.html', {'form':form})

# Post and details
def post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    return render(request,'post.html')







# Register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username = username,password=password)
            login(request,user)
            messages.success(request,('Registration successfull and logged in'))
            return redirect('dashboard')
           
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})

