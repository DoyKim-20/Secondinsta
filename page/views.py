from django.shortcuts import render
from .models import Model
# Create your views here.

def home(request):
    return render(request,'home.html')


def home(request):
    Models=Model.objects.all()
    return render(request, 'home.html', {'Models':Models})