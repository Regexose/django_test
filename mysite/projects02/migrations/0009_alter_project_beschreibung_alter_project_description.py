# Generated by Django 4.0.4 on 2023-07-15 07:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0008_project_kurzbeschreibung_project_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='beschreibung',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
