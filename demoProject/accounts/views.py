from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
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
            elif User.objects.filter(email=mail).exists():
                print('EMAIL taken')
            else:
            
            #Creating user from build-in function 
                user=User.objects.create_user(username=uname,password=pass1,email=mail,first_name=fname,last_name=lname)
                user.save()
                print('USER CREATED')
        else:
            print('PASSWORD DOES NOT MATCH')
        return redirect('/') #Return to home page after registering...
    else:
    #When register tab is pressed in index.html
        return render(request,"register.html")
    