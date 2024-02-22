from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{'Name':'Pooja','Age':'22'})

def add(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    result=n1+n2
    return render(request,'result.html',{'Result':result})