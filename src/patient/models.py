from django.db import models

from autoslug import AutoSlugField
from simple_history.models import HistoricalRecords
from versatileimagefield.fields import VersatileImageField

from config.models.baseModel import BaseModelWithUID

from .choices import PatientStatus
from .utils import get_patient_slug, get_patient_image_file_path


# Create your models here.
class Patient(BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_patient_slug, unique=True)
    image = VersatileImageField(
        upload_to=get_patient_image_file_path, blank=True, null=True
    )

    status = models.CharField(
        max_length=50,
        choices=PatientStatus.choices,
        default=PatientStatus.ACTIVE,
    )

    user = models.ForeignKey("core.User", on_delete=models.CASCADE)

    # Track changes in model
    history = HistoricalRecords()

    def __str__(self):
        return f"UID: {self.uid}, Name: {self.user.get_name()}"
