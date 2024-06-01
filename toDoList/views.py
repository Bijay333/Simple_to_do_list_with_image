from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        'persons' : [{"name" : "John", "age" : 28},
                     {"name" : "Olivia", "age" : 21},
                     {"name" : "Peter", "age" : 32},
                     {"name" : "Sam", "age" : 16},
                     ],
        }
    return render(request, 'index.html', context)

def contact(request):
    phone = 87451100
    return HttpResponse(f"<h1>Contact Us: {phone}</h1>")