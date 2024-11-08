from django.shortcuts import render

from .models import Todo



def index(request):
    data = Todo.objects.all()
    return render(request,'index.html',{"todos":data})


def create_todo(request):
    title = request.POST['title']
    todo = Todo.objects.create(title=title)
    data = Todo.objects.all()

    return render(request,'todo_list.html',{"todos":data})



def mark_todo(request,id):
    todo = Todo.objects.get(id=id)


    todo.complated = not todo.complated
    todo.save()
    data = Todo.objects.all()
    return render(request,'todo_list.html',{"todos":data})


def delete_todo(request,id):
    todo = Todo.objects.get(id=id)


    todo.delete()
    data = Todo.objects.all()
    return render(request,'todo_list.html',{"todos":data})
