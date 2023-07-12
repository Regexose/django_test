from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "projects02"
urlpatterns = [
                  path('', views.project_view, name='project'),
                  path('<int:id>/', views.detail_view, name='detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)