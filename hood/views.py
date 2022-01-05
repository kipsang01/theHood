from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from .forms import RegisterUserForm,newHoodForm, PostForm, BusinessForm,ServiceForm

from .models import Neighborhood, Post, Profile, HoodMember,Business,Service



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
    if hood_group is not None:
        hood = hood_group.hood
        posts =Post.objects.filter(neighborhood =hood)
        form = PostForm()
        context = {
            'hood':hood,
            'posts':posts,
            'form':form,
        }
        return render(request,'home.html', context)
    else:
        return redirect('dashboard')

# Creating new Neighborhood
@login_required(login_url='/accounts/login')
def new_hood(request):
    if request.method == 'POST':
        current_user = request.user
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


# Join a neighborhood
@login_required(login_url='/accounts/login')
def join_hood(request,hood_id):
    hood = get_object_or_404(Neighborhood,id=hood_id)
    new_member = HoodMember(member = request.user, hood= hood)
    new_member.save()
    messages.success(request,("You've joined the group"))
    return redirect('home')


# Leave neighborhood
def leave_hood(request,hood_id):
    current_user = request.user
    hood = get_object_or_404(Neighborhood,id=hood_id)
    membership = HoodMember(member = current_user, hood= hood)
    membership.delete()
    return redirect('dashboard')
    
    
    
# Creating newpost
@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == "POST":
        current_user = request.user
        hood_group = HoodMember.objects.filter(member=current_user).first()
        hood = hood_group.hood
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.neighborhood = hood
            post.save()
            messages.success(request,('Posted!'))
            message='posted successfully'
            return JsonResponse({'error': False, 'message': message},status=200)
    
        else:
            return JsonResponse({'error': True, 'errors': form.errors},status=400)
   

# Post and details
def post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    return render(request,'post.html')

# businesses
def business(request):
    current_user = request.user
    hood_group = HoodMember.objects.filter(member=current_user).first()
    hood = hood_group.hood
    businesses = Business.objects.filter(neighborhood =hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighborhood = hood
            business.save()
            new_member = HoodMember(member=current_user,hood=hood)
            new_member.save()
            messages.success(request,('Business Added!'))
            return redirect('business')
    else:
        form = BusinessForm()
    return render(request, 'business.html',{'form':form,'businesses':businesses })

#hospital
def hospital(request):
    current_user = request.user
    hood_group = HoodMember.objects.filter(member=current_user).first()
    hood = hood_group.hood
    hospitals = Service.objects.filter(type ='hospital',Neighborhood=hood)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.type = 'hospital'
            service.Neighborhood = hood
            service.save()
            new_member = HoodMember(member=current_user,hood=hood)
            new_member.save()
            messages.success(request,('Hospital added!'))
            return redirect('hospitals')
    else:
        form = ServiceForm()
    return render(request, 'hospitals.html',{'form':form,'hospitals':hospitals })

#school
def school(request):
    current_user = request.user
    hood_group = HoodMember.objects.filter(member=current_user).first()
    hood = hood_group.hood
    schools = Service.objects.filter(type ='school',Neighborhood=hood)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.type = 'school'
            service.Neighborhood = hood
            service.save()
            new_member = HoodMember(member=current_user,hood=hood)
            new_member.save()
            messages.success(request,('School added!'))
            return redirect('schools')
    else:
        form = ServiceForm()
    return render(request, 'schools.html',{'form':form, 'schools':schools})



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

