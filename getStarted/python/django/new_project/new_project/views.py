from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is home page of the new Django project!")
def about(request):
    return HttpResponse("Hello, this is about page of the new Django project!")
def contact(request):
    return HttpResponse("Hello, this is contact page of the new Django project!")