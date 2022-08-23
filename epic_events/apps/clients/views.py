from inspect import Attribute
from rest_framework import viewsets

# from project.permissions import CanEditClient
from .models import Client
# from apps.contracts.models import Contract
from user_management.models import UserModel
from .serializers import ClientSerializer
from project.permissions import ClientPermissions, IsManagement


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = [ClientPermissions | IsManagement ]
    search_fields = ('^first_name', '^last_name', '^email', '^company_name')
    filterset_fields = ('is_prospect', "id", "first_name", "last_name", "email")

    def get_queryset(self):

        """
        SALE Users can access their own clients, and all prospects
        """

        if self.request.user.usergroup == UserModel.UserGroup.SALE:
            clients = Client.objects.filter(sales_contact=self.request.user)
            prospects = Client.objects.filter(is_prospect=True)
            return prospects | clients
        if self.request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return Client.objects.filter(contract__event__support_contact=self.request.user)
            # The following is for Managers to still Access All clients, permissions will prevent access to
            # Unauthorized Usergroups
        return Client.objects.all()