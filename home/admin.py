from django.contrib import admin
from .models import SlideContent

# Register your models here.

class SlideContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
    )

    fields = (
        'name',
        'image',
        'title',
        'blurb',
    )

    ordering = ('name',)


admin.site.register(SlideContent, SlideContentAdmin)
