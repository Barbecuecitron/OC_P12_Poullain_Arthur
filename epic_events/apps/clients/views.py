from inspect import Attribute
from rest_framework import viewsets

from apps.contracts.views import get_support_related_contracts
from .models import Client
from apps.contracts.models import Contract
from user_management.models import UserModel
from .serializers import ClientSerializer
from project.permissions import ClientPermissions, IsManagement
import logging
logger = logging.getLogger('django')

# Return clients linked to events we are responsible for
def get_support_related_clients(user):
    clients = []
    for contract in get_support_related_contracts(user):
        if contract.client:
            clients.append(contract.client.id)
    return Client.objects.filter(id__in=clients)


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
            return get_support_related_clients(self.request.user)#Client.objects.filter(contract__event__support_contact=self.request.user)
            # The following is for Managers to still Access All clients, permissions will prevent access to
            # Unauthorized Usergroups
        return Client.objects.all()