from intro.views import instruction
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from . regform import pfform
from . regform import areaform
from . regform import familyform
from .models import Dprofile
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, render
import datetime
from django.db.models import Q


@login_required()
# Create your views here.

def registration(request):
    form = pfform()
    if request.method == 'POST':
        form = pfform(request.POST)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.userid = request.user.id
            frm.lastmodifieduserid = request.user.id
            frm.registrationdate = datetime.datetime.now()
            frm.lastmodifieddate = datetime.datetime.now()
            firstname = frm.firstname
            familyname = frm.familyname
            fathername = frm.fathername
            if not Dprofile.objects.filter(firstname = firstname, familyname = familyname, fathername = fathername).exists():
                frm.save()
                #return redirect('thankyou')
                return render(request,'thankyou.html')
            else:
                messages.success(request,  'This record is already entered. Please edit your record if you want. !')
                return render(request, 'registration.html', {'form': form})
            
        else:
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request,'registration.html',{'form':form})

def profileview(request):
    profiles = Dprofile.objects.all()
    return render(request,'profileview.html',{'profiles':profiles})

def edit(request):
    profiles = Dprofile.objects.filter(Q(userid=request.user.id))
    return render(request,'updateview.html',{'profiles':profiles})

def update(request,edit_id):
    profile = Dprofile.objects.get(id=edit_id)
    form = pfform(instance=profile)
    return render(request,'registration.html',{'form':form})

def regfamily(request):
    form = familyform()
    if request.method == 'POST':
        form = familyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('introd')
        else:
            messages.error(request, form.error_messages )
    else:
        return render(request,'registration.html',{'form':form})

def regarea(request):
    form = areaform()
    if request.method == 'POST':
        form = areaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('introd')
        else:
            messages.error(request, form.error_messages )
    else:
        return render(request,'registration.html',{'form':form})