from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    name = "John"
    return HttpResponse(f"<h1>Hello, {name}!</h1>")