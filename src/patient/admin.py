from django.contrib import admin
from .models import Patient


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = [
        "uid",
        "slug",
        "_name",
        "status",
    ]
    readonly_fields = ["uid", "slug"]

    def _name(self, obj: Patient) -> str:
        return obj.user.get_name()
