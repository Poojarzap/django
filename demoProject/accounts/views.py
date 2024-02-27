import django
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.contrib import messages

# Create your views here.

def logout(request):
    django.contrib.auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        upass=request.POST['pass']
        user = authenticate(request,username=username,password=upass)
        if user is not None:
            django.contrib.auth.login(request, user)
            print("LOGIN successfull")
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def register(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        mail=request.POST['email']


        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                print('USERNAME taken')
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                print('EMAIL taken')
                messages.info(request,'Email taken')
                return redirect('register')
            else:
            
            #Creating user from build-in function 
                user=User.objects.create_user(username=uname,password=pass1,email=mail,first_name=fname,last_name=lname)
                user.save()
                print('USER CREATED')
                return redirect('login')

        else:
            print('PASSWORD DOES NOT MATCH')
            messages.info(request,'Password doesnot match')
            return redirect('register')
        return redirect('/') #Return to home page after registering...
    else:
    #When register tab is pressed in index.html
        return render(request,"register.html")
    




        
    
    