from django.shortcuts import render
from django.utils import timezone
from .models import Project


def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "projects/project_list.html", {"projects": projects})
