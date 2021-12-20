from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from .forms import RegisterUserForm

# Create your views here.
def home(request):
    return render(request,'home.html')

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

