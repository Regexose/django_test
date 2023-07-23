# Generated by Django 4.0.4 on 2023-07-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0005_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='description_de',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_de',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
