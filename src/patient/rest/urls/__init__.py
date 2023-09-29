from django.urls import include, path

urlpatterns = [
    path("/medicines", include("patient.rest.urls.medicine")),
]
