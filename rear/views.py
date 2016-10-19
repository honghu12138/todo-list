# -*- encoding: utf-8 -*-
from django.shortcuts import render
from models import Todo 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def home(request):
    print("view goes here")
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
        elif action == "textchange":
            value = request.POST.get("id")
            todo = Todo.objects.get(id=value)
            todo.content = request.POST.get('value')
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
    else:
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

def get_todo(todos):
    import json
    todo = dict(
        content='todo',
        id=1,
        completed=True
    )
    return HttpResponse(json.dumps(todo))

@csrf_exempt
def todo(request):
    import json
    if request.method == 'POST':
        text = json.loads(request.body)
        # imput by jason
        todo = Todo(content=text.get("content"),state=False)
        todo.save() 
        id = todo.id
        value = todo.content
        todo = dict(
            content=value,
            id=id,
            state=False
        )
        response = HttpResponse(json.dumps(todo))
        #回复至jason网页
        response['content-type'] = 'application/json'
        return response
   
    elif request.method == 'GET':
         filter = request.GET.get('filter')
         if filter == 'completed':
               todos = Todo.objects.filter(state=True)
         elif filter == 'active':
             todos = Todo.objects.filter(state=False)
         else:
             todos = Todo.objects.all() 
         list=[ ]
         for todo in todos:
             todo = dict(
                content=todo.content,
                id=todo.id,
                completed=todo.state
             )
             list.insert(0,todo)
             #
         response = HttpResponse(json.dumps(list))
         response['content-type'] = 'application/json'
         return response
    else:
        return HttpResponse("",status=405)


@csrf_exempt
def edit_todo(request, id):
    if request.method == 'DELETE':
        try:   
            todo = Todo.objects.get(id=id)
            todo.delete()
            response = HttpResponse("",status=200)
            return response
        except Todo.DoesNotExist:
            return HttpResponse("", status=404)

    elif request.method == 'PUT':
          import json
          try:
              todo = Todo.objects.get(id=id)
              text = json.loads(request.body)
              if text.get('content') != None:
                  todo.content = text.get('content')
              if text.get('state') != None:
                  todo.state = text.get('state')
              todo.save()
              id = todo.id
              value = todo.content
              todo = dict(
                  content=todo.content,
                  id=todo.id,
                  state=todo.state
                  ) 
              response = HttpResponse(json.dumps(todo))
              response['content-type'] = 'application/json'  
              return response
          except Todo.DoesNotExist:
              return HttpResponse("",status=405)



    

