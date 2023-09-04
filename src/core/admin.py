from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("phone", "email", "is_active")
    list_editable = ("is_active",)
    search_fields = ("email", "phone")
    readonly_fields = (
        "id",
        "uid",
        "created_at",
        "updated_at",
        "date_joined",
        "password",
    )
