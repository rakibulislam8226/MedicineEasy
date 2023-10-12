from rest_framework import generics

from core.models import Organization

from account.rest.serializers.organizations import OrganizationSlimSerializer

from ..permissions import IsOrganizationAdminOrOwner


class OrganizationListView(generics.ListCreateAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer


class OrganizationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer
    permission_classes = [IsOrganizationAdminOrOwner]

    def get_object(self):
        organization_uid = self.kwargs.get("organization_uid", None)
        kwargs = {
            "uid": organization_uid,
        }
        organization = generics.get_object_or_404(
            Organization.objects.filter(), **kwargs
        )

        return organization
