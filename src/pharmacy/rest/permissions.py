from rest_framework.permissions import BasePermission

from account.choices import OrganizationUserRole, OrganizationUserStatus


class IsOrganizationStaff(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user

        profile = user.get_organization_user()

        if profile is not None and profile.status == OrganizationUserStatus.ACTIVE:
            return profile.role in [
                OrganizationUserRole.ADMIN,
                OrganizationUserRole.OWNER,
                OrganizationUserRole.STAFF,
            ]

        return False
