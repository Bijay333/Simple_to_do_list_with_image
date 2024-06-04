from django.shortcuts import render, HttpResponse, redirect
from toDoList.models import *

# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        task_image = request.FILES.get('task_image')
        
        task_name = data.get('task_name')
        task_description = data.get('task_description')
        
        Things_to_do.objects.create(
            task_image = task_image,
            task_name = task_name,
            task_description = task_description,
        )
        
        return redirect('/tasklist/')
    
    queryset = Things_to_do.objects.all()
    
    context = {
        "tasks" : queryset
    }

    return render(request, 'index.html', context)

def contact(request):
    phone = 87451100
    return HttpResponse(f"<h1>Contact Us: {phone}</h1>")