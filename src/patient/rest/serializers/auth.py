from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.choices import UserType
from patient.models import Patient

User = get_user_model()


class PatientAuthSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=50)
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "weight",
            "height",
            "date_of_birth",
            "gender",
            "blood_group",
            "password",
        )

    def validate_phone(self, value):
        if value and User.objects.filter(phone=value).exists():
            raise ValidationError("This phone number is already taken by another user.")
        return value

    def validate_email(self, value):
        if value and User.objects.filter(email=value).exists():
            raise ValidationError("This email already exists.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.pop("email", None)
        if email is not None:
            validated_data["email"] = email.lower()
        validated_data["height"] = validated_data.get("height", None)
        validated_data["weight"] = validated_data.get("weight", None)

        user = User.objects.create(
            password=make_password(password),
            type=UserType.PATIENT,
            is_active=True,
            **validated_data,
        )

        Patient.objects.create(user=user)

        return user
