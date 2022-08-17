from rest_framework import permissions
from user_management.models import UserModel
from apps.contracts.models import Contract
from rest_framework.exceptions import PermissionDenied

"""
General Permissions
"""


class IsManagement(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT


"""
Clients Related Permissions
"""

"""SELL can Update their own clients, 
    View all of clients
"""


class CanViewClients(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup in (
            UserModel.UserGroup.MANAGEMENT,
            UserModel.UserGroup.SALE,
        )

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


class ContractPermissions(permissions.BasePermission):
    """Sales team : can CREATE new contracts
                    can VIEW and UPDATE contracts of their own clients
    Support team : can VIEW their clients contracts
    """

    def has_permission(self, request, view):
        if request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.usergroup == UserModel.UserGroup.SALE

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.usergroup == UserModel.UserGroup.SUPPORT:
                return obj in Contract.objects.filter(
                    event__support_contact=request.user
                )
            return request.user == obj.sales_contact
        elif request.method == "PUT" and obj.status:
            raise PermissionDenied("Cannot update a signed contract.")
        return request.user == obj.sales_contact and obj.status is False
