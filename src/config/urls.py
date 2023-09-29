from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    ## Swagger
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/v1/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/docs/redoc",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # JWT token
    path("api/v1/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    # REST
    path("api-auth/", include("rest_framework.urls")),
    # Admin
    path("admin/", admin.site.urls),
    # Projects apps urls.
    # pharmacy
    path("api/v1/pharmacy", include("pharmacy.rest.urls")),
    # patients
    path("api/v1/patients", include("patient.rest.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
