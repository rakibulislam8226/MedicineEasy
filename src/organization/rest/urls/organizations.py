from django.urls import path

from ..views.organizations import OrganizationListView, OrganizationDetailView

urlpatterns = [
    path(
        "/<uuid:organization_uid>",
        OrganizationDetailView.as_view(),
        name="organization-detail",
    ),
    path("", OrganizationListView.as_view(), name="organization-list"),
]
