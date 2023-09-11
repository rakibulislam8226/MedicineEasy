from rest_framework import serializers

from pharmacy.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["uid", "name", "slug"]
        read_only_fields = ["uid"]
