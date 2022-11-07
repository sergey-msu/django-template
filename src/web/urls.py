from django.urls import path

from .views.projects import project_index, project_details


urlpatterns = [
    path("projects/", project_index, name="project_index"),
    path("projects/<int:pk>/", project_details, name="project_details"),
]
