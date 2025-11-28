from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/todo_list.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todoapp/add_todo.html', {'form': form})


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo_list')