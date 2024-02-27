# Demo Project for Django
Learnt from telusko yt channel<br>
Link is : https://www.youtube.com/watch?v=SIyxjRJ8VNY&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau&index=1

# Migration for database
python manage.py makemigrations <br>
python manage.py sqlmigrate travello 0001 <br>
python manage.py migrate <br>

# Super User
Name : pooja <br>
pass : 123 <br>
mail : pooja@gmail.com <br>

# Changes other than in Video
django.contrib.auth.logout(request) <br>
<pre>user = authenticate(request,username=username,password=upass)
        if user is not None:
            django.contrib.auth.login(request, user)
            print("LOGIN successfull")
            return redirect("/")</pre>