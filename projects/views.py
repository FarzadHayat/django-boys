from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Project
from .forms import ProjectForm


def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "projects/project_list.html", {"projects": projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projects/project_detail.html", {"project": project})


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.published_date = timezone.now()
            project.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, "projects/project_edit.html", {"form": form})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.author:
        return redirect("project_detail", pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.published_date = timezone.now()
            project.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/project_edit.html", {"form": form})


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.author:
        return redirect("project_detail", pk)
    project.image.delete()
    project.delete()
    return redirect("project_list")
