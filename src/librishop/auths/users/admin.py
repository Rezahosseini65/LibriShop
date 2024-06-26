from django.contrib import admin

from .models import CustomUser, Profile


# Register your models here.


class ProfileInLineAdmin(admin.StackedInline):
    model = Profile
    extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')

    inlines = [ProfileInLineAdmin]
