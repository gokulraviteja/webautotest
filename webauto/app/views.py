from django.shortcuts import render
from django.http import HttpResponse
from app.models import testelement
# Create your views here.
def home(request):
    if(request.method== 'POST'):
        p=request.POST['data']
        ele=testelement.objects.get(id='1')
        ele.value=p
        ele.save()
        return render(request,"app/display.html",{"ele":ele})
    else:
        return render(request,"app/home.html")

def display(request):
    if(request.method== 'POST'):
        p=request.POST['voicedata']
        ele=testelement.objects.get(id='1')
        ele.value=p
        ele.save()
        return render(request,"app/display.html",{"ele":ele})
    else:
        ele=testelement.objects.get(id='1')
        return render(request,"app/display.html",{"ele":ele})

def voice(request):
    return render(request,"app/voice.html")
