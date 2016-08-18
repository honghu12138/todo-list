# -*- encoding: utf-8 -*-
from django.shortcuts import render
from models import Todo 

#from django.template import loader.Context


# Create your views here.
def home(request):
    if request.method == "POST":
        value = request.POST.get('value')
        content = request.POST.get('content')
        state = request.POST.get('state')
        number = request.POST.get('number')
        todo = Todo(content=value,state=False)
        todo.save()
    todos = Todo.objects.all()  
    return render(request,"front.html",{
        'todos': todos,
        'count': count(todos) 
        })
    
    
def todochange(request):
    if request.method == "POST":
        value = request.POST.get("id")
        todo = Todo.objects.get(id=value)
        if todo.state == False:
            todo.state = True
        else:
            todo.state = False
        todo.save()
        todos = Todo.objects.all()    
        return render(request,"front.html",{
            'todos': todos,
            'count': count(todos)
        })

def tododelete(request):
     if request.method == "POST": 
         value = request.POST.get("id")
         todo = Todo.objects.get(id=value)
         todo.delete()
         todos = Todo.objects.all()
         return render(request,"front.html",{
            'count': count(todos),
            'todos': todos
        })
            
def completelist(request):
    if request.method == "POST":
        todos = Todo.objects.all()
        todos = Todo.objects.filter(state=True)
        return render(request,"front.html",{
            'count': count(todos),
            'todos': todos
        })

def uncompletelist(request):
    if request.method == "POST":
        todos = Todo.objects.all()
        todos = Todo.objects.filter(state=False)
        return render(request,"front.html",{
            'count': count(todos),
            'todos': todos
        })

def alltodos(request):
    if request.method == "POST":
        todos = Todo.objects.all()
        return render(request,"front.html",{
            'count': count(todos),
            'todos': todos
        })




def count(todos):
    number = 0
    for todo in todos:
        if todo.state == False:
            number = number + 1
        else:
            number = number  

    return  number


def textchange(request):
     if request.method == "POST": 
         value = request.POST.get("id")
         todo = Todo.objects.get(id=value)
         todo.content = request.POST.get('value')
         todo.save()
     todos = Todo.objects.all()    
     return render(request,"front.html",{
            'todos': todos,
            'count': count(todos)
        })

    

