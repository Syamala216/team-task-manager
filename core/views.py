from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkItem, Workspace, User
from datetime import date


# 🟢 DASHBOARD
@login_required
def dashboard(request):
    tasks = WorkItem.objects.filter(assigned_to=request.user)

    total = tasks.count()
    completed = tasks.filter(status='DONE').count()
    pending = tasks.filter(status='PENDING').count()

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
        'today': date.today()
    })


# 🟢 CREATE WORKSPACE
@login_required
def create_workspace(request):
    if request.method == 'POST':
        Workspace.objects.create(
            name=request.POST['name'],
            description=request.POST['desc'],
            created_by=request.user
        )
        return redirect('dashboard')

    return render(request, 'create_workspace.html')


# 🟢 CREATE TASK
@login_required
def create_task(request):
    users = User.objects.all()
    workspaces = Workspace.objects.all()

    if request.method == 'POST':
        WorkItem.objects.create(
            title=request.POST['title'],
            description=request.POST['desc'],
            assigned_to_id=request.POST['user'],
            workspace_id=request.POST['workspace'],
            due_date=request.POST['date']
        )
        return redirect('dashboard')

    return render(request, 'create_task.html', {
        'users': users,
        'workspaces': workspaces
    })


# 🟢 UPDATE TASK STATUS (NEW FEATURE 🚀)
@login_required
def update_status(request, task_id, status):
    task = get_object_or_404(WorkItem, id=task_id)

    # Only assigned user can update
    if task.assigned_to == request.user:
        task.status = status
        task.save()

    return redirect('dashboard')