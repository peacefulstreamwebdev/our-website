from django.contrib import admin
from .models import TeamContent, TeamMember

# Register your models here.

class TeamContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'team_content_blurb',
    )

    ordering = ('name',)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
    )

    fields = (
        'name',
        'title',
        'image',
        'twitter',
        'facebook',
        'instagram',
        'linkedin',
    )

    ordering = ('name',)


admin.site.register(TeamContent, TeamContentAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
