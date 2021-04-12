from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, ScreenForm, MacroForm, DeviceForm
from .models import Todo, Screen, Macro, Device
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import generic
from . import models
from . import forms


def home(request):
    screens = Screen.objects.filter(enabled=True)
    return render(request, 'autonomica/home.html', {'screens': screens})

def viewscreen(request, screen_pk):
    screen = get_object_or_404(Screen, pk=screen_pk)
    macro = Macro.objects.filter(screen_id=screen_pk).order_by('-name')
    device = Device.objects.filter(screen_id=screen_pk).order_by('-name')
    if request.method == 'GET':
        formS = ScreenForm(instance=screen)
        return render(request, 'autonomica/viewscreen.html', {'screen': screen, 'form': formS, 'macros': macro, 'devices': device})
    else:
        try:
            form = ScreenForm(request.POST, instance=screen)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'autonomica/viewtodo.html',
                          {'autonomica': screen, 'form': screen, 'error': 'Bad data'})



# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'autonomica/signupuser.html', {'form': UserCreationForm()})
    else:
        # Create new user.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'autonomica/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Username has been taken.'})
        else:
            return render(request, 'autonomica/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match.'})


@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    print(todos)
    return render(request, 'autonomica/currenttodos.html', {'todos': todos})


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'autonomica/completedtodos.html', {'todos': todos})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'autonomica/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'autonomica/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and PW did not match '})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'autonomica/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'autonomica/createtodo.html', {'error': 'Bad Data submitted'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'autonomica/viewtodo.html', {'autonomica': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'autonomica/viewtodo.html', {'autonomica': todo, 'form': form, 'error': 'Bad data'})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.delete()
        return redirect('currenttodos')



