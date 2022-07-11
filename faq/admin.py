from django.contrib import admin
from .models import FaqCategory, Faq

# Register your models here.

class FaqCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'date_created',
    )

    fields = (
        'name',
        'category',
        'question',
        'image',
        'answer',
        'tags',
    )

    ordering = ('name',)


admin.site.register(FaqCategory, FaqCategoryAdmin)
admin.site.register(Faq, FaqAdmin)