from inspect import Attribute
from rest_framework import viewsets

# from project.permissions import CanEditClient
from .models import Client
from user_management.models import UserModel

from .serializers import ClientSerializer
from rest_framework.permissions import IsAdminUser
from project.permissions import (
    CanViewClients,
    CanCreateClient,
    CanEditClient,
    IsManagement,
)


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    filterset_fields = ("id", "first_name", "last_name", "email")

    def get_queryset(self):

        """
        SALE Users can only access their own clients
        """

        if self.request.user.usergroup == UserModel.UserGroup.SALE:
            return Client.objects.filter(sales_contact=self.request.user)

        return Client.objects.all()

    def get_permissions(self):

        permission_classes = {
            "list": (CanViewClients,),
            "retrieve": (CanViewClients,),
            "create": (CanCreateClient,),
            "update": (CanEditClient,),
            "partial_update": (CanEditClient,),
            "default": (IsManagement,),
        }

        return [permission() for permission in permission_classes[self.action]]
