from django.contrib import admin
from .models import Content, BlackList

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

class BlackListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
    )

    fields = (
        'name',
        'email',
    )

    ordering = ('name',)


admin.site.register(BlackList, BlackListAdmin)
admin.site.register(Content, ContentAdmin)