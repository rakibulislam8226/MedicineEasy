from django.urls import path
from ..views.pharmacy import PharmacyListView

urlpatterns = [
    path("", PharmacyListView.as_view(), name="pharmacy-list"),
]
