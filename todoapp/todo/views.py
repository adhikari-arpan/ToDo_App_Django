from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        text = request.POST['todo']
        todo = Todo.objects.create(text=text)
        todo.save()
        return redirect('index')
    
    return render(request,'index.html',{'todos':todos})

def delete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('index')

def edit_todo(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.text = request.POST['todo']
        todo.save()
        return redirect('index')
    return render(request,'edit.html',{'todo':todo})