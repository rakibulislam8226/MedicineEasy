from django.urls import include, path

urlpatterns = [
    path("/search-medicine", include("patient.rest.urls.medicine")),
]
