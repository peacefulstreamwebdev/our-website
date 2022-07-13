from django.contrib import admin
from .models import ProjectCategory, Project

# Register your models here.

class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
    )

    fields = (
        'name',
        'category',
        'image',
        'link',
    )

    ordering = ('name',)


admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)