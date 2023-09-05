from django.contrib import admin
from .models import (
    Medicine,
    Generic,
    SideEffect,
    Brand,
    StorageInstructions,
    MedicineInteraction,
    GuidelinesForChildren,
    Pharmacology,
    DosageGuidelines,
)


# Register your models here.
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    list_display = ["uid", "name", "brand"]
    readonly_fields = ["uid"]


@admin.register(DosageGuidelines)
class DosageGuidelinesAdmin(admin.ModelAdmin):
    model = DosageGuidelines
    list_display = ["uid", "period", "food_time", "pices"]
    readonly_fields = ["uid"]


@admin.register(GuidelinesForChildren)
class GuidelinesForChildrenAdmin(admin.ModelAdmin):
    model = GuidelinesForChildren
    list_display = ["uid", "age_group", "short_guideline"]
    readonly_fields = ["uid"]


@admin.register(Pharmacology)
class PharmacologyAdmin(admin.ModelAdmin):
    model = Pharmacology
    list_display = ["uid", "mechanism_of_action"]
    readonly_fields = ["uid"]


@admin.register(MedicineInteraction)
class MedicineInteractionAdmin(admin.ModelAdmin):
    model = MedicineInteraction
    list_display = ["uid", "interaction_severity"]
    readonly_fields = ["uid"]


@admin.register(StorageInstructions)
class StorageInstructionsAdmin(admin.ModelAdmin):
    model = StorageInstructions
    list_display = ["uid", "place"]
    readonly_fields = ["uid"]


@admin.register(Generic)
class GenericAdmin(admin.ModelAdmin):
    model = Generic
    list_display = ["uid", "name"]
    readonly_fields = ["uid"]


@admin.register(SideEffect)
class SideEffectAdmin(admin.ModelAdmin):
    model = SideEffect
    list_display = ["uid", "effect"]
    readonly_fields = ["uid"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ["uid", "name"]
    readonly_fields = ["uid"]
