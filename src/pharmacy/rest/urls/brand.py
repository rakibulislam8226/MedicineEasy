from django.urls import path
from ..views.brand import BrandListView, BrandDetailView

urlpatterns = [
    path("", BrandListView.as_view(), name="brand-list"),
    path("/<uuid:brand_uid>", BrandDetailView.as_view(), name="brand-detail"),
]
