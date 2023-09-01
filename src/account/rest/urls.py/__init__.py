from django.urls import include, path

urlpatterns = [
    path("/pharmacy", include("account.rest.urls.pharmacy")),
    path("/patients", include("account.rest.urls.patients")),
]
