from rest_framework import permissions
from user_management.models import UserModel
from apps.contracts.models import Contract
from apps.clients.models import Client
from rest_framework.exceptions import PermissionDenied

"""
General Permissions
"""
# See the settings file

""" Managers have read_only permissions on the crm.
Post, put or delete has to be done via the admin site.
"""

class IsManagement(permissions.BasePermission):
    def has_permission(self, request, view):
        print("Vous êtes le manager")
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT and request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        print("Vous êtes le manager de l'objet")
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT and request.method in permissions.SAFE_METHODS


class ClientPermissions(permissions.BasePermission):
    """ Sales team : can CREATE new clients / prospects
                     can VIEW and UPDATE any prospect and their own clients
                     can DELETE prospects only
        Support team : can VIEW clients of their own contracts
    """
    def has_permission(self, request, view):
        if request.user.usergroup == UserModel.UserGroup.MANAGEMENT:
            return request.method in permissions.SAFE_METHODS
        return request.user.usergroup in (UserModel.UserGroup.SALE,UserModel.UserGroup.SUPPORT)
    

    def has_object_permission(self, request, view, obj):
        if request.user.usergroup == UserModel.UserGroup.SALE:
            if request.method == 'DELETE':
                return request.user.usergroup == UserModel.UserGroup.SALE and obj.is_prospect is True
            else:
                return obj.sales_contact == request.user or obj.is_prospect
        elif request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return obj in Client.objects.filter(contract__event__support_contact=request.user)
        # raise PermissionDenied('You are not allowed to access this content')


class ContractPermissions(permissions.BasePermission):
    
    """Sales team : can CREATE new contracts
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
            return True
        else:
            raise PermissionDenied("Cannot update a signed contract.")
        # return request.user == obj.sales_contact and obj.status is False

class EventPermissions(permissions.BasePermission):

    """ Sales team : can CREATE new events
                     can VIEW events of their own clients
                     can UPDATE events of their own clients if not finished
        Support team : can VIEW events of their own clients
                       can UPDATE events of their own clients if not finished
    """

    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)