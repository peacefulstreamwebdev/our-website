from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'company',
    )

    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
