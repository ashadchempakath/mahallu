from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('',views.register,name='usersignup'),
    path('accounts/login',views.login,name='userlogin'),
    path('logout/', auth.LogoutView.as_view(template_name ='login.html'), name ='logout'),
]
