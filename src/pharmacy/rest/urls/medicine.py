from django.urls import path
from ..views.medicine import MedicineListView

urlpatterns = [
    path("", MedicineListView.as_view(), name="medicine-list"),
]
