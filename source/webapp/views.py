from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
from webapp.forms import TaskForm


def index_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks
    })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def task_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                date_perf=form.cleaned_data['date_perf'],
                detail = form.cleaned_data['detail']

            )

            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'status': task.status,
            'date_perf': task.date_perf,
            'detail': task.detail
        })
        return render(request, 'update.html', context={
            'form': form,
            'task': task
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.date_perf = form.cleaned_data['date_perf']
            task.detail = form.cleaned_data['detail']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
