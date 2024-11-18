from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/<username>/',views.find_user,name='find-user'),
    path('dashbord/',views.dashboard,name='dashbord'),
    path('logout/',views.user_logout,name='logout')
]
