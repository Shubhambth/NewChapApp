from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
User = get_user_model()

def index(request):
    return render(request,'index.html')


def user_login(request):
    if request.method== "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password") 
        if all([username,password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            
    return render(request,'login.html',{})   



def user_register(request):
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
      user = User.objects.create_user(username=username,email=email,password=password)
      user.save()
      return redirect('login')
    except:
      return render(request,'registeration.html',{})
  return render(request, 'registeration.html',{})
        

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        
        profile = request.user.profile
    
    return render(request, 'profile.html', {'profile':profile})

def find_user(request,username):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        
        profile = request.user.profile
    
    return render(request, 'profile.html', {'profile':profile}) 


def dashboard(request):
   return render(request,'dashbord.html')
    
   



