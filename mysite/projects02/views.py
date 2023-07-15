from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'detail_grid.html', {
        'project': project,
        'photos': photos
    })
