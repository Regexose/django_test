# Generated by Django 4.2.3 on 2023-07-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects02', '0013_alter_project_embed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectembed',
            options={'ordering': ['-added']},
        ),
        migrations.AddField(
            model_name='projectembed',
            name='added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]