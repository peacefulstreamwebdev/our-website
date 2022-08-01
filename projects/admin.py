from django.contrib import admin
from .models import Project, Stage

# Register your models here.

class StageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'project',
    )

    fields = (
        'name',
        'project',
        'progress',
        'target_date',
        'latest_update',
        'date_updated',
    )

    ordering = (
        'name',
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'completed',
    )

    readonly_fields = ('project_id', )

    fields = (
        'project_id',
        'name',
        'user',
        'repo',
        'completed',
    )

    ordering = ('name',)


admin.site.register(Stage, StageAdmin)
admin.site.register(Project, ProjectAdmin)