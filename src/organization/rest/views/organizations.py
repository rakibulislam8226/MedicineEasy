from rest_framework import generics

from core.models import Organization

from account.rest.serializers.organizations import OrganizationSlimSerializer


class OrganizationListView(generics.ListCreateAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer


class OrganizationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSlimSerializer

    def get_object(self):
        organization_uid = self.kwargs.get("organization_uid", None)
        kwargs = {
            "uid": organization_uid,
        }
        brand = generics.get_object_or_404(Organization.objects.filter(), **kwargs)

        return brand
