from django.urls import include, path

urlpatterns = [
    path("", include("organization.rest.urls.organizations")),
]
