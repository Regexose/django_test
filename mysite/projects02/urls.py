from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "projects02"
urlpatterns = [
                  path('', views.project_view, name='project'),
                  path('home/', views.index_view, name='index'),
                  path('<int:id>/', views.detail_view, name='detail')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)