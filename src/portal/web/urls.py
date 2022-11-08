from django.urls import path

from .views.projects import project_index, project_details
from .views.blog import blog_index, blog_detail, blog_category


urlpatterns = [
    # home
    path("", project_index, name="project_index"),

    # projects
    path("projects/", project_index, name="project_index"),
    path("projects/<int:pk>/", project_details, name="project_details"),

    # blog
    path("blog/", blog_index, name="blog_index"),
    path("blog/<int:pk>/", blog_detail, name="blog_detail"),
    path("blog/<category>/", blog_category, name="blog_category"),
]
