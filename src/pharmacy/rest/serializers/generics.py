from rest_framework import serializers

from pharmacy.models import Generic


class GenericListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generic
        fields = ["uid", "name", "slug"]
        read_only_fields = ["uid"]
