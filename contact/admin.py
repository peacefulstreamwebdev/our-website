from django.contrib import admin
from .models import Content

# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'google_maps_link',
        'address',
        'address_two',
        'email',
        'phone',
    )

    ordering = ('name',)


admin.site.register(Content, ContentAdmin)