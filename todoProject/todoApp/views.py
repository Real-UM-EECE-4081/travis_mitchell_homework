from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from datetime import datetime, timedelta


def project_list(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        Project.objects.create(name=name)
        return redirect('project_list')

    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')


def task_list(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        description = request.POST.get('description', '')
        category = request.POST.get('category', '')
        expected_time_to_complete_str = request.POST.get('expected_time_to_complete', '')
        h, m, s = map(int, expected_time_to_complete_str.split(':'))  # New line
        expected_time_to_complete = timedelta(hours=h, minutes=m, seconds=s) if expected_time_to_complete_str else None
        due_date_str = request.POST.get('due_date', '')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
        priority = request.POST.get('priority', '')
        Task.objects.create(project=project, description=description, category=category,
                            expected_time_to_complete=expected_time_to_complete, due_date=due_date, priority=priority)
        return redirect('task_list', pk=pk)

    tasks = Task.objects.filter(project=project)
    return render(request, 'task_list.html', {'project': project, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list', pk=task.project.pk)


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.completion_date = datetime.now().date()
    task.save()
    return redirect('task_list', pk=task.project.pk)
