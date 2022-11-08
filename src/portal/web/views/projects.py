from django.shortcuts import render
from ...data.db_context import DATA


def project_index(request):
    projects = DATA.get_all_projects()
    context = { 'projects': projects }
    return render(request, 'project_index.html', context)


def project_details(request, pk):
    project = DATA.get_project_by_id(pk)
    context = { 'project': project }
    return render(request, 'project_details.html', context)
