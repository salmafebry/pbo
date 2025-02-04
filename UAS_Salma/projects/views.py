from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Menampilkan daftar proyek
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

# Membuat proyek baru
@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

# Menampilkan detail proyek dan daftar tugasnya
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()  # Mengambil semua tugas dalam proyek
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

# Membuat tugas baru dalam proyek
@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

# Mengupdate status tugas
@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=task.project.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'task': task})

# Menghapus tugas
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id
    task.delete()
    return redirect('project_detail', project_id=project_id)
