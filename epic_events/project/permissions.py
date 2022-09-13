from rest_framework import permissions
from user_management.models import UserModel
from apps.contracts.models import Contract
from apps.clients.models import Client
from apps.events.models import Event
from rest_framework.exceptions import PermissionDenied

"""
General Permissions
"""
# See the settings file

""" Managers have read_only permissions on the crm.
    Post, put or delete has to be done through the admin site.
"""

class IsManagement(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT and request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT and request.method in permissions.SAFE_METHODS


class ClientPermissions(permissions.BasePermission):
    
    """ Sales team : can CREATE new clients / prospects
                     can VIEW and UPDATE any prospect and their own clients
                     can DELETE prospects only
        Support team : can VIEW clients of their own contracts
    """
    def has_permission(self, request, view):
        if request.user.usergroup in (UserModel.UserGroup.MANAGEMENT, UserModel.UserGroup.SUPPORT):
            return request.method in permissions.SAFE_METHODS
        return request.user.usergroup == UserModel.UserGroup.SALE

    def has_object_permission(self, request, view, obj):
        if request.user.usergroup == UserModel.UserGroup.SALE:
            if request.method == 'DELETE':
                return request.user.usergroup == UserModel.UserGroup.SALE and obj.is_prospect
            else:
                return obj.sales_contact == request.user or obj.is_prospect
        elif request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return request.method in permissions.SAFE_METHODS #obj in Client.objects.filter(contract__event__support_contact=request.user)
        # raise PermissionDenied('You are not allowed to access this content')


class ContractPermissions(permissions.BasePermission):
    
    """ Sales team : can CREATE new contracts
                     can VIEW contracts and UPDATE contracts of their clients until signed
        Support team : can VIEW their clients contracts
    """

    def has_permission(self, request, view):
        if request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return request.method in permissions.SAFE_METHODS
        return request.user.usergroup == UserModel.UserGroup.SALE

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # if request.user.usergroup == UserModel.UserGroup.SUPPORT:
            #     return obj in Contract.objects.filter(
            #         event__support_contact=request.user
            #     )
            return request.user == obj.sales_contact or request.user == obj.event__support_sales_contact
        elif request.method == "PUT" and obj.status == "OPEN":
            return request.user.usergroup == UserModel.UserGroup.SALE
        else:
            raise PermissionDenied("Cannot update a signed contract.")

class EventPermissions(permissions.BasePermission):

    """ Sales team : can CREATE new events
                     can VIEW events of their own clients
                     can UPDATE events of their own clients if not finished
        Support team : can VIEW events of their own clients
                       can UPDATE events of their own clients if not finished
    """

    def has_permission(self, request, view):
        mtd = request.method

        if request.user.usergroup == UserModel.UserGroup.MANAGEMENT:
            return mtd in permissions.SAFE_METHODS

        if request.user.usergroup in (UserModel.UserGroup.SUPPORT):
            return mtd not in ("DELETE", "CREATE")

        return mtd != "DELETE"

    def has_object_permission(self, request, view, obj):
        mtd = request.method

        if mtd in permissions.SAFE_METHODS:
            return request.user in (obj.contract.sales_contact, obj.support_contact)
        if mtd in ("PUT","CREATE"):
            return request.user in (obj.contract.sales_contact, obj.support_contact)