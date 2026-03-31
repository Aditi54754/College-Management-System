from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets



class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Create your views here.

def register(request):
    if request.method == 'POST':
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error' :'Username Already Exists'})      

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email =email,
            username=username,
            password=password
            )
        
        Profile.objects.create(
            user = user,
            role = role
        )
        return redirect('login')
    return render(request,'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('main_page')
    return render(request,'login.html')

@login_required
def main_page(request):
    user = request.user
    if Profile.objects.filter(user=user).exists():
        user_profile = Profile.objects.filter(user=user).last()
        return render (request,'main_page.html',{'profile':user_profile})  
    return redirect('login')
