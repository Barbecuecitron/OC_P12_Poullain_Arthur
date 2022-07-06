from rest_framework import permissions
from user_management.models import UserModel
import logging



class IsManagement(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup == UserModel.UserGroup.MANAGEMENT


class CanViewClients(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.usergroup in (
            UserModel.UserGroup.MANAGEMENT,
            UserModel.UserGroup.SALE,
        )

    def has_object_permission(self, request, view, obj):
        logging.debug("Object permission")
        if request.user.usergroup == UserModel.UserGroup.SALE:
            logging.debug(obj.sales_contact == request.user)
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
