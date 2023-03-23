from django.shortcuts import render


def home_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'dashboard/home.html', context)


def task_view(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/task_list.html', context)
