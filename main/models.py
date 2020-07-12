from django.db import models
from datetime import datetime

# Create your models here.
# TutorialCategory -> TutorialSeries -> Tutorial
class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        verbose_name = "Categories"

    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    category = models.ForeignKey(TutorialCategory, default=None, verbose_name="Category", on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        verbose_name = "Series"

    def __str__(self):
        return self.series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("Date Published", default=datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries, default=None, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=None)
    objects = models.Manager()

def __str__(self):
    return self.tutorial_title