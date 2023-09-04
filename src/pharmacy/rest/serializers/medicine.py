from rest_framework import serializers

from pharmacy.models import Drug, Brand, Generic


class MedicineListSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field="uid", queryset=Brand.objects.filter()
    )
    generic = serializers.SlugRelatedField(
        slug_field="uid", queryset=Generic.objects.filter()
    )

    class Meta:
        model = Drug
        fields = [
            "uid",
            "name",
            "slug",
            "brand",
            "presentation",
            "batch_no",
            "manufacturer",
            "expiry_date",
            "generic",
            "side_effect",
            "storage_instructions",
            "dosage_guidelines",
            "drug_interaction",
            "guidelines_for_children",
            "pharmacology",
        ]
        read_only_fields = ["uid", "slug"]
