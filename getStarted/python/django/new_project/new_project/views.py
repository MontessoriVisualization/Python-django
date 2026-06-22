from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'about/aboutus.html')
def contact(request):
    return HttpResponse("Hello, this is contact page of the new Django project!")