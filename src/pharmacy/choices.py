from django.db import models


class PresentationChoice(models.TextChoices):
    TABLET = "TABLET", "Tablet"
    CAPSULE = "CAPSULE", "Capsule"
    SYRUP = "SYRUP", "Syrup"

class PeriodType(models.TextChoices):
    MORNING = "MORNING", "Morning"
    NOON = "NOON", "Noon"
    AFTERNOON = "AFTERNOON", "Afternoon"
    EVENING = "EVENING", "Evening"
    NIGHT = "NIGHT", "Night"


class MedicineTime(models.TextChoices):
    BEFORE = "BEFORE", "Before Eat"
    AFTER = "AFTER", "After Eat"
    MINTIME = "MINTIME", "Mintime of Eat"