from django.db import models
#from https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/
from ckeditor.fields import RichTextField
# https://www.youtube.com/watch?v=Rh7THG1-THU

class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    titel= models.CharField(max_length=250, blank=True)
    short_description = models.CharField(max_length=250, blank=True)
    kurzbeschreibung = models.CharField(max_length=250, blank=True)
    # description = models.TextField(blank=True)
    # beschreibung = models.TextField(blank=True)
    description = RichTextField(blank=True, null=True)
    beschreibung = RichTextField(blank=True, null=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='pics/')

    def __str__(self):
        return self.project.title