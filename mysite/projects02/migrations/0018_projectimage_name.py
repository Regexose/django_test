# Generated by Django 4.0.4 on 2023-08-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0017_rename_images_projectimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
