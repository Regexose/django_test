# Generated by Django 4.2.3 on 2023-07-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0011_rename_projectvideo_projectembed'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='embed',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]