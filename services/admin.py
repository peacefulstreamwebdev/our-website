from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'icon_color',
        'icon_class',
        'description',
    )

    ordering = ('name',)


admin.site.register(Service, ServiceAdmin)