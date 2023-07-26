from django.db import models
from django import forms
from django.urls import reverse
#from https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/
from ckeditor.fields import RichTextField
# https://www.youtube.com/watch?v=Rh7THG1-THU
from embed_video.fields import EmbedVideoField

class Project(models.Model):
    FEATURED = (
        ('Y', 'YES'),
        ('N', 'NO')
    )
    title = models.CharField(max_length=250, blank=True)
    titel= models.CharField(max_length=250, blank=True)
    short_description = models.CharField(max_length=250, blank=True)
    kurzbeschreibung = models.CharField(max_length=250, blank=True)
    description = RichTextField(blank=True, null=True)
    beschreibung = RichTextField(blank=True, null=True)
    image = models.FileField(blank=True)
    embed = models.URLField(max_length= 250, blank=True)
    featured = models.CharField(max_length=10, blank=True, choices=FEATURED)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='pics/')

    def __str__(self):
        return self.project.title

class ProjectEmbed(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    video = EmbedVideoField(default=None, blank=True)
    added = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-added']