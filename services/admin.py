from django.contrib import admin
from .models import Service, Content, Feature

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'icon_color',
        'icon_class',
        'svg_path',
        'description',
    )

    ordering = ('name',)


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'features_description',
    )

    ordering = ('name',)


class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'icon_color',
        'icon_class',
    )

    ordering = ('name',)    



admin.site.register(Service, ServiceAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Feature, FeatureAdmin)