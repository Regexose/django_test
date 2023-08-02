from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage, ProjectEmbed
import random

def index_view(request):
    featured = Project.objects.get(featured='Y')
    projects = Project.objects.all()
    context = {'projects': projects,
               'featured': featured
               }
    return render(request, 'index.html', context)

def project_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def detail_carousel(request, id):
    projects = Project.objects.all()
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    ph_size = len(ProjectImage.objects.filter(project=project))
    embeds = ProjectEmbed.objects.filter(project=project)
    return render(request, 'detail_carousel.html', {
        'projects': projects,
        'project': project,
        'photos': photos,
        'ph_size': ph_size,
        'embeds': embeds
    })

def detail_view(request, id):
    projects = Project.objects.all()
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    embeds = ProjectEmbed.objects.filter(project=project)
    return render(request, 'detail_grid.html', {
        'projects': projects,
        'project': project,
        'photos': photos,
        'embeds': embeds
    })
