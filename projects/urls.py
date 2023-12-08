from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("project/new/", views.project_new, name="project_new"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("project/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("project/<int:pk>/delete/", views.project_delete, name="project_delete"),
]
