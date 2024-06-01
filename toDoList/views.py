from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    phone = 87451100
    return HttpResponse(f"<h1>Contact Us: {phone}</h1>")