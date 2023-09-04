from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pharmacy", include("pharmacy.rest.urls")),
    path("api/v1/patient", include("patient.rest.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
