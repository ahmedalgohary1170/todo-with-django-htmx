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

