from django.contrib import admin

from account.models import Organization, OrganizationUser


# Register your models here.


class OrganizationUserInlineAdmin(admin.TabularInline):
    model = OrganizationUser
    fk_name = "organization"
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = [
        "uid",
        "name",
    ]
    inlines = (OrganizationUserInlineAdmin,)


@admin.register(OrganizationUser)
class OrganizationUserAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ["uid", "role", "user", "organization", "is_default"]
    list_filter = ("role",)
