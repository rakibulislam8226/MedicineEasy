from rest_framework import generics

from core.models import Organization

from account.rest.serializers.organizations import OrganizationSlimSerializer


class OrganizationListView(generics.ListCreateAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer
