from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request,'rooms/index.html')

def examples (request):
        return render(request,'rooms/examples.html')
