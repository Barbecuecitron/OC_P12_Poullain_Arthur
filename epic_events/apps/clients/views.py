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

from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("id",)

    def get_queryset(self):
        print("Get queryset est appelé")
        """
        Filterset_fields and foreign keys seem to be really unstable within ModelViewsets.
        We will instead manually retrieve passed-in URL parameters, and apply them as filters on the queryset,
        to get full control on whats going on. 
        """
        queryset = Client.objects.all()
        url_sales_contact = self.request.query_params.get("sales_contact")
        if url_sales_contact is not None:
            queryset = queryset.filter(sales_contact__email=url_sales_contact)
        return queryset

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
