# -*- encoding: utf-8 -*-
from django.shortcuts import render
from models import Todo 





# Create your views here.
def home(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "add":
            value = request.POST.get('value')
            todo = Todo(content=value,state=False)
            todo.save()
            todos = Todo.objects.all()
        elif action == "todochange":
            value = request.POST.get("id")
            todo = Todo.objects.get(id=value)
            if todo.state == False:
                todo.state = True
            else:
                todo.state = False
            todo.save()
            todos = Todo.objects.all()
        elif action == "tododelete":
            value = request.POST.get("id")
            todo = Todo.objects.get(id=value)
            todo.delete()
            todos = Todo.objects.all()
        elif action == "completelist":
            todos = Todo.objects.all()
            todos = Todo.objects.filter(state=True)
        elif action == "uncompletelist":
            todos = Todo.objects.all()
            todos = Todo.objects.filter(state=False)
        elif action == "alltodos":
            todos = Todo.objects.all() 
    return render(request,"front.html",{
        'todos': todos,
        'count': count(todos) 
        })
    





def count(todos):
    number = 0
    for todo in todos:
        if todo.state == False:
            number = number + 1
        else:
            number = number  

    return  number


    

    

