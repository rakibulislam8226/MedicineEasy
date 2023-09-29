from rest_framework import generics

from account.models import Organization
from account.rest.serializers.organizations import OrganizationSlimSerializer

from ..permissions import IsOrganizationStaff


class PharmacyListView(generics.ListAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer
    permission_classes = [IsOrganizationStaff]
