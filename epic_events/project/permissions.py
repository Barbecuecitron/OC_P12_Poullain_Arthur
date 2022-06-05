from rest_framework import permissions
from user_management.models import User_Model
from rest_framework.exceptions import PermissionDenied

class IsSupport(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.usergroup == "Support":
            return True
        return False

class IsSale(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.usergroup == User_Model.UserGroup.SALE:
            return True
        return False

class AlwaysFalse(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
