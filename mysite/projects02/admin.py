from django.contrib import admin

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
class ProjectImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectEmbed)
class ProjectEmbedAdmin(admin.ModelAdmin):
    pass