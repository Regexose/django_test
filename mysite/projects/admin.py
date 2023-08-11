from django.contrib import admin
from .models import Image
import admin_thumbnails

@admin_thumbnails.thumbnail('photo')
class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)

