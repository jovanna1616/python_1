# Generated by Django 3.0.8 on 2020-07-12 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200712_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_slug',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 20, 13, 39, 630079), verbose_name='Date Published'),
        ),
    ]