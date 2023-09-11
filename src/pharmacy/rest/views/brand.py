from rest_framework import generics

from pharmacy.models import Brand

from ..permissions import IsOrganizationStaff
from ..serializers.brand import BrandListSerializer


class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.filter()
    serializer_class = BrandListSerializer
    permission_classes = [IsOrganizationStaff]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandListSerializer
    permission_classes = [IsOrganizationStaff]

    def get_object(self):
        brand_uid = self.kwargs.get("brand_uid", None)
        kwargs = {
            "uid": brand_uid,
        }
        brand = generics.get_object_or_404(Brand.objects.filter(), **kwargs)

        return brand
