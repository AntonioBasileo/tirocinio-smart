from rest_framework.permissions import BasePermission


def _get_user_from_request(request):
    return getattr(request, "user", None)

def _user_is_authenticated(user):
    return getattr(user, "is_authenticated", False)

class CompanyPermissions(BasePermission):

    def has_permission(self, request, view):
        user = _get_user_from_request(request)

        if not _user_is_authenticated(user):
            return False

        if request.method == "GET":
            return user.has_perm("app.company_view")

        return user.has_perm("app.admin_view")

class TrainingPermissions(BasePermission):

    def has_permission(self, request, view):
        user = _get_user_from_request(request)

        if not _user_is_authenticated(user):
            return False

        return user.has_perm("app.training_register_view") or user.has_perm("app.admin_view")