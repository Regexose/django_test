from django.contrib import admin
import admin_thumbnails

from .models import Project, ProjectImage, ProjectEmbed

class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage

class ProjectEmbedAdmin(admin.StackedInline):
    model = ProjectEmbed

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project


@admin.register(ProjectImage)
@admin_thumbnails.thumbnail('image')
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumbnail')

@admin.register(ProjectEmbed)
class ProjectEmbedAdmin(admin.ModelAdmin):
    pass