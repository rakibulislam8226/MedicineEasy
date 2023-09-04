from rest_framework import generics, filters

from rest_framework.permissions import IsAuthenticated

from pharmacy.models import Drug

from ..serializers.medicine import MedicineListSerializer
from ..permissions import IsOrganizationStaff


class MedicineListView(generics.ListCreateAPIView):
    queryset = Drug.objects.filter()
    permission_classes = [IsOrganizationStaff]
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
