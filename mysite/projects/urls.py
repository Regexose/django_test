from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "projects"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:project_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.detail, name="project_detail"),
    path("all/", views.all_images, name='all_images')
]
