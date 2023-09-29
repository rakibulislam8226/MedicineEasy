from django.urls import path

from ..views.auth import PatientAuthListView

urlpatterns = [
    path("/signup", PatientAuthListView.as_view(), name="patient-auth"),
]
