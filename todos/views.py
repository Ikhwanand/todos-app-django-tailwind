from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo

# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todos/index.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        if title:
            Todo.objects.create(
                user=request.user,
                title=title,
                description=description
            )
            messages.success(request, 'Todo added successfully!')
        else:
            messages.error(request, 'Title is required!')
    return redirect('todos:index')

@login_required
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')

@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todos:index')

@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        if title:
            todo.title = title
            todo.description = description
            todo.save()
            messages.success(request, 'Todo updated successfully!')
        else:
            messages.error(request, 'Title is required!')
    return redirect('todos:index')

