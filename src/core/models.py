from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from rest_framework.exceptions import ValidationError

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from config.models.baseModel import BaseModelWithUID
from account.models import Organization, OrganizationUser

from .choices import UserStatus, UserType, UserGender, BloodGroups
from .managers import CustomUserManager
from .utils import get_user_slug, get_user_media_path_prefix


class User(AbstractBaseUser, BaseModelWithUID, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(unique=True, db_index=True, verbose_name="Phone Number")
    slug = AutoSlugField(populate_from=get_user_slug, unique=True)
    nid = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    image = VersatileImageField(
        "Image",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    type = models.CharField(max_length=20, choices=UserType.choices)
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.ACTIVE,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    blood_group = models.CharField(
        max_length=10,
        blank=True,
        choices=BloodGroups.choices,
        default=BloodGroups.NOT_SET,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return f"UID: {self.uid}, Phone: {self.phone}"

    def get_name(self):
        name = " ".join([self.first_name, self.last_name])
        return name.strip()
    
    def get_organization_user(self) -> OrganizationUser:
        try:
            return self.organizationuser_set.select_related("organization", "user").get(
                is_default=True
            )
        except OrganizationUser.DoesNotExist:
            raise ValidationError({"detail": "You do not have any organization!"})

    def get_organization(self) -> Organization:
        try:
            organizationuser = self.get_organization_user()
        except Organization.DoesNotExist:
            raise ValidationError({"detail": "Organization not found!"})

        return organizationuser.organization

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_joined = timezone.now()
        self.username = self.phone
        super().save(*args, **kwargs)
