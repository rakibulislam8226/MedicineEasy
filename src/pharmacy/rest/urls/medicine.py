from django.urls import path
from ..views.medicine import MedicineListView, MedicineDetailView

urlpatterns = [
    path("", MedicineListView.as_view(), name="medicine-list"),
    path("/<uuid:medicine_uid>", MedicineDetailView.as_view(), name="medicine-detail"),
]
