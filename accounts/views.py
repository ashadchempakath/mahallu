from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .signupform import customSignupforms
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# from django.contrib.auth import forms
# from django.shortcuts import redirect, render
# from django.http.response import HttpResponse
# from accounts.signupform import customSignupforms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.urls import reverse

#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = customSignupforms(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            # htmly = get_template('user/Email.html')
            # d = { 'username': username }
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = customSignupforms()
    return render(request, 'registration/signup.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('introd')
        else:
            messages.info(request, f'account done not exit please sign in')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'title':'log in'})



# #Create your views here.
# def signup_view(request):
#     form = UserCreationForm()
#     #form = customSignupforms()
#     if request.method == 'POST':
#         #form = customSignupforms(request.POST)
#         form = customSignupforms(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'The form is valid.')
#             print('successfully registered')
#             return redirect('login')
#         else:
#             messages.error(request, form.error_messages )
#             print(form.error_messages)
#            # return HttpResponse(form.errors.values())
             
#     return render(request,'registration/signup.html', {'form':form})
