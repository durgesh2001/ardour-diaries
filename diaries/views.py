from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def work(request):
    return render(request,"work.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")    


def poetries(request):
    poem = poems.objects.all()
    return render(request,"poetries.html",{'poem' : poem})  

def shayries(request):
    shayry = shayri.objects.all()
    return render(request,"shayries.html",{'shayry' : shayry})  

def oneliner(request):
    oneline = oneliners.objects.all()
    return render(request,"oneliner.html",{'oneline' : oneline})  

def poeme(request,pk):
    poem1 = poems.objects.get(id=pk)
    return render(request,"poeme.html", {'poem1' : poem1})    

def shayrees(request,sk):
    shayri1 = shayri.objects.get(id=sk)
    return render(request,"shayrees.html", {'shayri1' : shayri1})    

def onelines(request,ok):
    oneline1 = oneliners.objects.get(id=ok)
    return render(request,"onelines.html", {'oneline1' : oneline1})    


