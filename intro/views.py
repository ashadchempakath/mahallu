from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'introduction.html')
    
def instruction(request):
    return render(request,'instruction.html')

def contact(request):
     return render(request,'contact.html')

def about(request):
     return render(request,'about.html')

