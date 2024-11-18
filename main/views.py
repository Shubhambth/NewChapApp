from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
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
                return redirect('create_profile')
            
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
        
@login_required(login_url='/login/')
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        
        profile = request.user.profile
    
    return render(request, 'profile.html', {'profile':profile})


@login_required(login_url='/login/')
def find_user(request,username):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        
        profile = request.user.profile
    
    return render(request, 'profile.html', {'profile':profile}) 

@login_required(login_url='/login/')
def dashboard(request):
   return render(request,'dashbord.html')


def user_logout(request):
  auth.logout(request)
  return redirect('home')

@login_required(login_url='/login/')
def search_profiles(request):
    query = request.GET.get('q', '')  # Get the search query
    if query:
        profiles = Profile.objects.filter(user__username__icontains=query)
    else:
        profiles = Profile.objects.all()  # Display all profiles if no search query
    
    return render(request, 'search_profiles.html', {'profiles': profiles, 'query': query})




@login_required(login_url='/login/')
def create_profile(request):
    # Check if the user already has a profile
    if Profile.objects.filter(user=request.user).exists():
        return redirect('search_profiles')  # Redirect if the profile already exists

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate profile with the logged-in user
            profile.save()
            return redirect('home', username=request.user.username)
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html', {'form': form})
    
   



