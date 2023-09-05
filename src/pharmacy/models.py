from django.db import models

from autoslug import AutoSlugField

from config.models.baseModel import BaseModelWithUID

from .choices import PresentationChoice, PeriodType, MedicineTime
from .utils import (
    get_dosage_guidelines_slug,
    get_storage_instructions_slug,
    get_medicine_slug,
)


class DosageGuidelines(BaseModelWithUID):
    """How to use the Medicine. When have to use."""

    period = models.CharField(max_length=255, choices=PeriodType.choices)
    food_time = models.CharField(
        max_length=255, choices=MedicineTime.choices, default=MedicineTime.AFTER
    )
    slug = AutoSlugField(populate_from=get_dosage_guidelines_slug, unique=True)
    pices = models.PositiveIntegerField(default=1)
    comment = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.period}"


class Pharmacology(BaseModelWithUID):
    """Information about how the body processes and eliminates the medicine"""

    mechanism_of_action = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.mechanism_of_action}"


class GuidelinesForChildren(BaseModelWithUID):
    """Specify the age group the guidelines are intended for (e.g., infant, child, adolescent)"""

    age_group = models.CharField(max_length=10, help_text="e.g. 1-10 or 10-15..")
    guideline = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.age_group}"

    @property
    def short_guideline(self):
        return (
            self.guideline if len(self.guideline) < 35 else (self.guideline[:33] + "..")
        )


class MedicineInteraction(BaseModelWithUID):
    """Explanation of how the medicines interact"""

    interaction_severity = models.CharField(max_length=100)
    interaction_mechanism = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.interaction_severity}"


class StorageInstructions(BaseModelWithUID):
    """Conditions or situations where the medicine should not be used"""

    place = models.CharField(
        max_length=100,
        help_text="Where have to store it. (e.g., cool place, lighty place etc)",
    )
    slug = AutoSlugField(populate_from=get_storage_instructions_slug, unique=True)

    def __str__(self) -> str:
        return f"{self.place}"


class Brand(BaseModelWithUID):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class SideEffect(BaseModelWithUID):
    effect = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.effects}"


class Generic(BaseModelWithUID):
    name = models.CharField(max_length=100, help_text="Napa from paracetamol.")
    slug = AutoSlugField(populate_from="name", unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Medicine(BaseModelWithUID):
    name = models.CharField(
        max_length=100, unique=True, help_text="This is the medicine name."
    )
    slug = AutoSlugField(populate_from=get_medicine_slug, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    presentation = models.CharField(
        max_length=255,
        choices=PresentationChoice.choices,
        default=PresentationChoice.TABLET,
    )
    batch_no = models.PositiveIntegerField(null=True, blank=True)
    manufacturer = models.DateField()
    expiry_date = models.DateField()
    generic = models.ForeignKey(Generic, on_delete=models.RESTRICT)
    side_effect = models.ForeignKey(
        SideEffect, on_delete=models.RESTRICT, null=True, blank=True
    )
    storage_instructions = models.ForeignKey(
        StorageInstructions, on_delete=models.RESTRICT, null=True, blank=True
    )
    dosage_guidelines = models.ForeignKey(
        DosageGuidelines, on_delete=models.RESTRICT, null=True, blank=True
    )
    medicine_interaction = models.ForeignKey(
        MedicineInteraction, on_delete=models.RESTRICT, null=True, blank=True
    )
    guidelines_for_children = models.ForeignKey(
        GuidelinesForChildren, on_delete=models.RESTRICT, null=True, blank=True
    )
    pharmacology = models.ForeignKey(
        Pharmacology, on_delete=models.RESTRICT, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Medicine"
        verbose_name_plural = "Medicine"
