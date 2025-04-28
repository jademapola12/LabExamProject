
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.contrib.auth.models import User
    

def project_list(request):
    # Fetching projects of the logged-in user (your projects)
    projects = Project.objects.filter(owner=request.user)

    # Fetching projects of other users (other projects)
    other_projects = Project.objects.exclude(owner=request.user)

    return render(request, 'project_list.html', {
        'projects': projects,
        'other_projects': other_projects,
    })
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    other_projects = Project.objects.exclude(owner=request.user)

    print("Your Projects:", projects)  # Debugging line
    print("Other Projects:", other_projects)  # Debugging line

    return render(request, 'project_list.html', {
        'projects': projects,
        'other_projects': other_projects,
    })
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    other_projects = Project.objects.exclude(owner=request.user)
    return render(request, 'project_list.html', {'projects': projects, 'other_projects': other_projects})

def home(request):
    return render(request, 'home.html')

def home(request):
    tasks = Task.objects.all()  # Ensure tasks have a valid pk
    return render(request, 'home.html', {'tasks': tasks})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form, 'task': task})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    return render(request, 'project_confirm_delete.html', {'project': project})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":

        task.title = request.POST.get('title')  
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('project_detail', pk=task.project.pk)  
    return render(request, 'task_edit.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('project_detail', pk=task.project.pk)
    
@login_required
def home(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'home.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def task_create(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=pk)
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'project': project})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
