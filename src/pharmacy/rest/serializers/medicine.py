from rest_framework import serializers

from pharmacy.models import (
    Medicine,
    Brand,
    Generic,
    GuidelinesForChildren,
    Pharmacology,
    SideEffect,
    StorageInstructions,
    DosageGuidelines,
    MedicineInteraction,
)


class MedicineInteractionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineInteraction
        fields = ["uid", "interaction_severity", "interaction_mechanism"]
        read_only_fields = ["uid"]


class DosageGuidelinesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageGuidelines
        fields = ["uid", "period", "food_time", "pices", "comment"]
        read_only_fields = ["uid"]


class StorageInstructionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageInstructions
        fields = ["uid", "place"]
        read_only_fields = ["uid"]


class PharmacologyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacology
        fields = ["uid", "mechanism_of_action"]
        read_only_fields = ["uid"]


class SideEffectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideEffect
        fields = ["uid", "effect"]
        read_only_fields = ["uid"]


class GuidelinesForChildrenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidelinesForChildren
        fields = ["uid", "age_group", "guideline"]
        read_only_fields = ["uid"]


class MedicineListSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field="uid", queryset=Brand.objects.filter()
    )
    generic = serializers.SlugRelatedField(
        slug_field="uid", queryset=Generic.objects.filter()
    )

    pharmacology = PharmacologyListSerializer()
    side_effect = SideEffectListSerializer()
    storage_instructions = StorageInstructionsListSerializer()
    dosage_guidelines = DosageGuidelinesListSerializer()
    medicine_interaction = MedicineInteractionListSerializer()
    guidelines_for_children = GuidelinesForChildrenListSerializer()

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

    def create(self, validated_data):
        """Get or create the realted fields for this medicine."""

        pharmacology_data = validated_data.pop("pharmacology")
        side_effect_data = validated_data.pop("side_effect")
        storage_instructions_data = validated_data.pop("storage_instructions")
        guidelines_for_children_data = validated_data.pop("guidelines_for_children")
        dosage_guidelines_data = validated_data.pop("dosage_guidelines")
        medicine_interaction_data = validated_data.pop("medicine_interaction")

        pharmacology, _ = Pharmacology.objects.get_or_create(**pharmacology_data)
        side_effect, _ = SideEffect.objects.get_or_create(**side_effect_data)
        storage_instructions, _ = StorageInstructions.objects.get_or_create(
            **storage_instructions_data
        )
        dosage_guidelines, _ = DosageGuidelines.objects.get_or_create(
            **dosage_guidelines_data
        )
        guidelines_for_children, _ = GuidelinesForChildren.objects.get_or_create(
            **guidelines_for_children_data
        )
        medicine_interaction, _ = MedicineInteraction.objects.get_or_create(
            **medicine_interaction_data
        )

        medicine = Medicine.objects.create(
            pharmacology=pharmacology,
            side_effect=side_effect,
            storage_instructions=storage_instructions,
            dosage_guidelines=dosage_guidelines,
            guidelines_for_children=guidelines_for_children,
            medicine_interaction=medicine_interaction,
            **validated_data
        )
        return medicine
