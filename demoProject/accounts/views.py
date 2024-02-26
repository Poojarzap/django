from django.shortcuts import render

# Create your views here.
def register(request):
    # dests=Destination.objects.all()
    return render(request,"register.html")
    