from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from .forms import RegisterUserForm,newHoodForm

from .models import Neighborhood, Post



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
def home(request,neighborhood_id):
    posts =Post.objects.filter(id =neighborhood_id).all()
    context = {
        'posts':posts
    }
    return render(request,'home.html', context)

def new_hood(request):
    if request.method == 'POST':
        pass
    else:
        form = newHoodForm()
    return render(request,'new-hood.html', {'form':form})

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
            return redirect('home')
           
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})

