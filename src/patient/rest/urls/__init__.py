from django.urls import include, path

urlpatterns = [
    path("/medicine", include("patient.rest.urls.medicine")),
]
