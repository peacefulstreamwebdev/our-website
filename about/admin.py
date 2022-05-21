from django.contrib import admin
from .models import TeamContent, TeamMember, SkillsContent, Skills

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


class SkillsContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'skills_content_blurb',
    )

    ordering = ('name',)


class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    fields = (
        'name',
        'skill',
    )

    ordering = ('name',)


admin.site.register(TeamContent, TeamContentAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(SkillsContent, SkillsContentAdmin)
admin.site.register(Skills, SkillsAdmin)