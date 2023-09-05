from django.urls import path

from ..views.medicine import PublicMedicineListView

urlpatterns = [
    path("", PublicMedicineListView.as_view(), name="public-medicine"),
]
