from django.contrib import admin

from librishop.auths.users.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
