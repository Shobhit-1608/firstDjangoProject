
from .models import Destination
from django.shortcuts import render

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Delhi"
    return render(request,'index.html',{'dest1':dest1})