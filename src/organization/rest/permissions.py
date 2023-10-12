from rest_framework.permissions import BasePermission
from rest_framework.generics import get_object_or_404

from account.choices import OrganizationUserRole, OrganizationUserStatus

from account.models import Organization


class IsOrganizationAdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        profile = user.get_organization_user()
        organization = user.get_organization()

        organization_uid = request.parser_context["kwargs"].get("organization_uid")
        request_organization = get_object_or_404(Organization, uid=organization_uid)

        if request_organization == organization:
            if profile is not None and profile.status == OrganizationUserStatus.ACTIVE:
                return profile.role in [
                    OrganizationUserRole.ADMIN,
                    OrganizationUserRole.OWNER,
                ]

            return False
