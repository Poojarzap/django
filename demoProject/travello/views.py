from django.shortcuts import render

from .models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name = 'Udupi'
    dest1.desc = 'City with beautiful hearts'
    dest1.img = 'destination_1.jpg'
    dest1.price = 1000

    dest2=Destination()
    dest2.name = 'Mulki'
    dest2.desc = 'City with beautiful cats'
    dest2.img = 'destination_2.jpg'
    dest2.price = 999

    dest3=Destination()
    dest3.name = 'Brahmavara'
    dest3.desc = 'City with beautiful dogs'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1900

    dest = [dest1,dest2,dest3]
    return render(request,"index.html",{'dests':dest})