from django.urls import include, path

urlpatterns = [
    path("/medicine", include("pharmacy.rest.urls.medicine")),
    path("/brand", include("pharmacy.rest.urls.brand")),
    path("/generics", include("pharmacy.rest.urls.generics")),
]
