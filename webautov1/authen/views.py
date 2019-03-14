from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .models import command_db,current_db
# Create your views here.

def insert(request):
    if(request.user.is_authenticated):
        if(request.method=="POST"):
            p=request.POST['voicedata']
            new=command_db.objects.create(command=p)
            q=command_db.objects.all()
            cur=current_db.objects.get(id=1)
            cur.current=q[0].command
            cur.save()
            return render(request,'display.html',{'q':q,'cur':cur.current})
        else:
            q=command_db.objects.all()
            if(len(q)!=0):
                cur=current_db.objects.get(id=1)
                cur.current=q[0].command
                cur.save()
            else:
                cur=current_db.objects.get(id=1)
                cur.current=1
                cur.save()

            return render(request,'display.html',{'q':q,'cur':cur.current})

    else:
        return render(request,'authen/home.html')


def checker(request):
    if(request.method=='POST'):
        instr_exe=cur=current_db.objects.get(id=1)
        q=command_db.objects.all()
        if(instr_exe.current!=1):

            q=command_db.objects.all()
            if(len(q)>0):
                q[0].delete()
                q=command_db.objects.all()
                cur=current_db.objects.get(id=1)
            if(len(q)>=1):
                cur.current=q[0].command
            else:
                cur.current=1
            cur.save()
        return render(request,'display.html',{'q':q,'cur':cur.current})
    else:
        q=command_db.objects.all()
        cur=current_db.objects.get(id=1)
        return render(request,'display.html',{'q':q,'cur':cur.current})










def home(request):
    if(request.user.is_authenticated):
        return render(request,'authen/index.html')
    else:
        return render(request,'authen/home.html')

def profile(request):
    if(request.user.is_authenticated):
        return render(request,'profile.html',{"user":request.user})
    else:
        return render(request,'authen/login.html',{"error_msg":""})
def commands(request):
    if(request.user.is_authenticated):
        return render(request,'commands.html',{"user":request.user})
    else:
        return render(request,'authen/login.html',{"error_msg":""})



def logout(request):
    auth_logout(request)
    return render(request,'authen/login.html')






def register(request):
    if(request.user.is_authenticated):
        return render(request,'authen/index.html')
    if(request.method=='POST'):
        q=User.objects.filter(email=request.POST['email'])
        if(len(q)!=0):
            return render(request,'authen/register.html',{"error_msg":"EMAIL ALREADY EXISTS!"})
        q=User.objects.filter(username=request.POST['uname'])
        if(len(q)!=0):
            return render(request,'authen/register.html',{"error_msg":"USERNAME ALREADY EXISTS!"})

        user=User.objects.create_user(email=request.POST['email'],username=request.POST['uname'],password=request.POST['pass'])

        auth_login(request,user)

        return render(request,'authen/index.html')

    else:
        return render(request,'authen/register.html',{"error_msg":""})


#key--  482457838952539
#pass--  6a75d822af66cdcf1db2e856bb05f54f

def login(request):
    if(request.user.is_authenticated):
        return render(request,'authen/index.html')
    if(request.method=='POST'):
        q=User.objects.filter(email=request.POST['email'])
        if(len(q)==0):
            return render(request,'authen/login.html',{"error_msg":"EMAIL DOESNOT EXIST!"})
        else:
            uname=q[0].username
            user=authenticate(username=uname,password=request.POST['pass'])
        if(user is None):
            return render(request,'authen/login.html',{"error_msg":"INVALID CREDENTIALS!"})

        auth_login(request,user)

        return render(request,'authen/index.html')

    else:
        return render(request,'authen/login.html',{"error_msg":""})
