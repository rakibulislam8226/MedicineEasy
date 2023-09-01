from django.urls import include, path

urlpatterns = [
    path("/medicine", include("pharmacy.rest.urls.medicine")),
]
