from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Todo
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo = request.POST['todo']
            if todo:
                created = Todo.objects.create(todo=todo,user=request.user)
        todos = Todo.objects.filter(user=request.user)
        print(todos)
        return render(request,'index.html',{'todos':todos})
    else:
        return redirect('login')
def edit(request,id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    if request.method == 'POST':
        edit_todo = request.POST['todo']
        todo_object = Todo.objects.filter(id=id)
        todo_object.update(todo=edit_todo)
        todo = Todo.objects.get(id=id)
        context = {'todo':todo}
    return render(request,'todo.html',context)

def delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("index")
# FOR CREATING USER 
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username,password=password)
            if user:
                return redirect("login")
    return render(request,'signup.html')

# LOGIN THE USER
def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect('index')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect("login")
