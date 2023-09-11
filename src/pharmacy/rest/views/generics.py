from rest_framework import generics

from pharmacy.models import Generic

from ..permissions import IsOrganizationStaff
from ..serializers.generics import GenericListSerializer


class GenericsListView(generics.ListCreateAPIView):
    queryset = Generic.objects.filter()
    serializer_class = GenericListSerializer
    permission_classes = [IsOrganizationStaff]


class GenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenericListSerializer
    permission_classes = [IsOrganizationStaff]

    def get_object(self):
        generic_uid = self.kwargs.get("generic_uid", None)
        kwargs = {
            "uid": generic_uid,
        }
        generic = generics.get_object_or_404(Generic.objects.filter(), **kwargs)

        return generic
