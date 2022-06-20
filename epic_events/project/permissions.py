from rest_framework import permissions
from user_management.models import UserModel
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser

# viewing_actions = ["list", "retrieve"]
# modifying_actions = ["create", ""]


class CanViewClients(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup in (UserModel.UserGroup.MANAGEMENT,)

    def has_object_permission(self, request, view, obj):
        if request.user.usergroup == UserModel.UserGroup.SALE:
            return obj.sales_contact == request.user
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT


class CanCreateClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.usergroup == UserModel.UserGroup.SALE:
            print("Vous pouvez créer le client")
            return True
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT


class CanEditClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.usergroup == UserModel.UserGroup.SALE:
            return obj.sales_contact == request.user
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT


class AlwaysFalse(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
