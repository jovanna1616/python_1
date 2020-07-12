from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):

    # fields = ('tutorial_title', 'tutorial_content', 'tutorial_published')
    fields = (('tutorial_title', 'tutorial_published'), 'tutorial_slug', 'tutorial_content', 'tutorial_series')


admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)
