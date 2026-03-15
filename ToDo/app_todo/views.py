from django.shortcuts import render, redirect
from .models import TODO
from .forms import NewTODOForm

# Create your views here.

def todo_list(request):
    data = TODO.objects.all()
    return render(request, 'app_todo/todo_list.html', {'data': data})

def list_one(request, id):
    data = TODO.objects.get(id=id)
    return render(request, 'app_todo/list_one.html', {'data': data})

def add_todo(request):
    if request.method == 'POST':
        form = NewTODOForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('add_todo')
            return redirect('todo_list')
    elif request.method == 'GET':
        form = NewTODOForm()
        return render(request, 'app_todo/add_todo.html', {'form': form})