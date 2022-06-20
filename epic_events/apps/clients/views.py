from rest_framework import viewsets

# from project.permissions import CanEditClient
from .models import Client
from user_management.models import UserModel
from .serializers import ClientSerializer
from rest_framework.permissions import IsAdminUser
from project.permissions import (
    CanViewClients,
    CanCreateClient,
    AlwaysFalse,
    CanEditClient,
)


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__()

    # def get_queryset(self):
    #     if self.request.user.UserGroup == "UserModel.UserGroup.SALE":
    #         queryset = Client.objects.filter(sales_contact=self.request.user)
    #     else:
    #         queryset = []
    #     return queryset

    def get_permissions(self):
        if self.action in ("list",):
            permission_classes = [CanViewClients]
        elif self.action in ("create", "retrieve"):
            permission_classes = [CanCreateClient]
        elif self.action in ("update", "partial_update"):
            permission_classes = [CanEditClient]
        else:
            print("Methode refusées:")
            print(self.action)
            permission_classes = [AlwaysFalse]
        return [permission() for permission in permission_classes]

    # return super().get_permissions()
