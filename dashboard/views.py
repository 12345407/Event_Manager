from django.shortcuts import render, HttpResponse
from.models import Task
from.forms import TaskForm


def home_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    tasks = Task.objects.all()
    form = TaskForm()
    print(form)

    return render(request, 'dashboard/home.html', {'tasks': tasks, 'form': form})


def task_view(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/task_list.html', context)
