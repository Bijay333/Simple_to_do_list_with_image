from django.shortcuts import render, redirect
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
    
    if request.GET.get('search'):
        queryset = queryset.filter(task_name__icontains = request.GET.get('search'))
    
    context = {
        "tasks" : queryset
    }

    return render(request, 'index.html', context)

def delete(request, pk):
    queryset = Things_to_do.objects.get(pk=pk)
    
    queryset.delete()
    return redirect('/tasklist/')

def update(request, pk):
    queryset = Things_to_do.objects.get(pk=pk)
    
    if request.method == "POST":
        data = request.POST
        task_image = request.FILES.get('task_image')
        
        task_name = data.get('task_name')
        task_description = data.get('task_description')
        
        queryset.task_name = task_name
        queryset.task_description = task_description
        
        if task_image:
            queryset.task_image = task_image
        
        queryset.save()
        
        return redirect('/tasklist/')
    
    context ={
        'tasks' : queryset
    }
    return render(request, 'update.html', context)