from rest_framework import permissions
from user_management.models import User_Model
from rest_framework.exceptions import PermissionDenied

group_based_permissions = {

    # Clients related permissions

    "view_all_clients": 
        [
            User_Model.UserGroup.SALE,
            User_Model.UserGroup.MANAGEMENT
        ],

    "create_clients":
        [
            User_Model.UserGroup.SALE
        ],

    "edit_clients":
        [
            User_Model.UserGroup.SALE
        ],

    # Contracts related permissions

    "create_contracts":
        [
            User_Model.UserGroup.SALE
        ],

    "sign_contracts":
        [
            User_Model.UserGroup.SALE
        ],

    # Events related permissions

    "add_event_to_contract":
        [
            User_Model.UserGroup.SALE
        ],

    "view_events":
        [
            User_Model.UserGroup.SUPPORT
        ]
        
}


class CanViewClients(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.usergroup in group_based_permissions['view_all_clients']:
            return True

class CanCreateClient(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.usergroup in group_based_permissions['create_clients']:
            return True
        return False

class CanEditClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.sales_contact)
        if obj.sales_contact == request.user:
            return True
        else:
            return False


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