from rest_framework import permissions
from user_management.models import User_Model
from rest_framework.exceptions import PermissionDenied

allowed_to_view_all = [
        User_Model.UserGroup.SUPPORT,
        User_Model.UserGroup.SALE,
        User_Model.UserGroup.MANAGEMENT
    ]

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

class CanViewClients(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.usergroup in allowed_to_view_all:
            return True

class CanEditClient(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print(obj.sales_contact)
        if obj.sales_contact == request.user:
            return True 
        else:
            return False