from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login

from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def activity(request):
    return render(request,'activity.html')

def register(request):
    error=""
    if request.method=="POST":
        reml=request.POST['reml']
        rpcd=request.POST['rpcd']
        rf=request.POST['rfnm']
        rl=request.POST['rlnm']
        rmob=request.POST['rmob']
        rrole=request.POST['rop']
        try:
            ruser=User.objects.create_user(username=reml,password=rpcd,first_name=rf,last_name=rl)
            Signup.objects.create(user=ruser,contact=rmob,role=rrole)
            error="no"
        except:
            error="yes"
    d={'error':error}
    
    return render(request,'register.html',d)    
         
def userlogin(request):
    error=""
    if request.method=='POST':
        un=request.POST['leml']
        pcd=request.POST['lpcd']
        
        
        user=authenticate(username=un,password=pcd)
        try:
            if user:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    
    dic={'error':error} 
    return render(request,'userlogin.html',dic);
    
#making views for userpanel

def portfolio(request):
    return render(request,'portfolio.html');

def announce(request):
    error=""
    if request.method=="POST":
        ann=request.POST['ann']

        try:
            Announce.objects.create(user=User.email, adata=ann)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'announce.html',d);

def event(request):
    error=""
    if request.method=="POST":
        d=request.POST['date']
        t=request.POST['time']
        v=request.POST['venue']
        evt=request.POST['evt']
        epg=request.POST['eping']

        try:
            Event.objects.create(user=User.email,edate=d,etime=t,evenue=v,edata=evt,eping=epg)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'event.html',d);

def userlogout(request):
    logout(request)
    return redirect('index')

def feed(request):
    error=""
    if request.method=="POST":
        fdata=request.method['feed']
        try:
            Feed.objects.create(user=User.email,fdata=fdata)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'feed.html',d)

def portprofile(request):
    return render(request,'portprofile.html')