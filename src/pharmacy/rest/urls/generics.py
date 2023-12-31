from django.urls import path

from ..views.generics import GenericsListView, GenericDetailView

urlpatterns = [
    path("/<uuid:generic_uid>", GenericDetailView.as_view(), name="generic-detail"),
    path("", GenericsListView.as_view(), name="generic-list"),
]
