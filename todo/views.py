from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from .forms import SignUpForm, TaskForm
from .models import Task

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('status', 'end_time')
    return render(request, 'task_list.html', {'tasks': tasks})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form,
                                              'form_title': 'New Task',
                                              'button_label': 'Create'})

@login_required
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        task.delete()
    return redirect('task_list')
@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form
                                              , 'form_title':'Edit Task',
                                              'button_label': 'Update'})