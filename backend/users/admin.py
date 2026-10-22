from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "max_documents", "last_login")
    list_filter = ("role", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Platform", {"fields": ("role", "avatar", "max_documents", "max_storage_bytes")}),
    )