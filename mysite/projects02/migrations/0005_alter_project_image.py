# Generated by Django 4.0.4 on 2023-07-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
