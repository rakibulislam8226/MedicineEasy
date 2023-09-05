from rest_framework import serializers

from pharmacy.models import Medicine, Brand, Generic

from pharmacy.rest.serializers.medicine import (
    SideEffectListSerializer,
    StorageInstructionsListSerializer,
    DosageGuidelinesListSerializer,
    MedicineInteractionListSerializer,
    GuidelinesForChildrenListSerializer,
    PharmacologyListSerializer,
)


class PublicMedicineListSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field="uid", queryset=Brand.objects.filter()
    )
    generic = serializers.SlugRelatedField(
        slug_field="uid", queryset=Generic.objects.filter()
    )
    side_effect = SideEffectListSerializer()
    storage_instructions = StorageInstructionsListSerializer()
    dosage_guidelines = DosageGuidelinesListSerializer()
    medicine_interaction = MedicineInteractionListSerializer()
    guidelines_for_children = GuidelinesForChildrenListSerializer()
    pharmacology = PharmacologyListSerializer()

    class Meta:
        model = Medicine
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
            "medicine_interaction",
            "guidelines_for_children",
            "pharmacology",
        ]
        read_only_fields = ["uid", "slug"]
