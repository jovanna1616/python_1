# Generated by Django 3.0.8 on 2020-07-12 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200712_1426'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='tutorial',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 14, 28, 39, 334300), verbose_name='Date Published'),
        ),
    ]