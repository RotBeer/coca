from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'coca/index.html')

def something(request):
    return render(request, 'coca/something.html')