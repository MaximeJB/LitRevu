from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserApp


@admin.register(UserApp)
class CustomUserAdmin(UserAdmin):
    pass
