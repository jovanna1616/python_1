# Generated by Django 3.0.8 on 2020-07-12 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200712_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.AddField(
            model_name='tutorialseries',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 20, 12, 20, 375344), verbose_name='Date Published'),
        ),
    ]
