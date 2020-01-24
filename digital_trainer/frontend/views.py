from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def module(request):
    return render(request, 'frontend/module.html')

def movement(request):
    return render(request, 'frontend/movement.html')

