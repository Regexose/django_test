# Generated by Django 4.0.4 on 2023-07-09 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='date published'),
        ),
    ]
