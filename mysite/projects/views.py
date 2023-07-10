from django.shortcuts import render, get_object_or_404
from .models import Project, Image

def index(request):
    latest_project_list = Project.objects.order_by('pub_date')[:5]
    context = {"latest_project_list": latest_project_list}
    return render(request, "projects/index.html", context)

def all_images(request):
    data = Image.objects.all()
    context = {'data': data}
    return render(request, "projects/display_all.html", context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "projects/detail.html", {"project": project})

