from django.db import models
#from https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/

class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    titel= models.CharField(max_length=250, blank=True)
    short_description = models.CharField(max_length=250, blank=True)
    kurzbeschreibung = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    beschreibung = models.TextField(blank=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='pics/')

    def __str__(self):
        return self.project.title