from rest_framework import generics, filters

from pharmacy.models import Drug

from ..serializers.medicine import MedicineListSerializer


class MedicineListView(generics.ListCreateAPIView):
    queryset = Drug.objects.filter()
    filter_backends = (filters.SearchFilter,)
    serializer_class = MedicineListSerializer
    search_fields = [
        "name",
        "brand__name",
        "side_effect__effect",
        "drug_interaction__interaction_severity",
        "drug_interaction__interaction_mechanism",
        "dosage_guidelines__period",
        "dosage_guidelines__food_time",
        "dosage_guidelines__comment",
        "guidelines_for_children__guideline",
        "pharmacology__mechanism_of_action",
    ]
