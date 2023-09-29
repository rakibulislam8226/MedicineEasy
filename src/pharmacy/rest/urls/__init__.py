from django.urls import include, path

urlpatterns = [
    path("/medicines", include("pharmacy.rest.urls.medicine")),
    path("/brands", include("pharmacy.rest.urls.brand")),
    path("/generics", include("pharmacy.rest.urls.generics")),
]
