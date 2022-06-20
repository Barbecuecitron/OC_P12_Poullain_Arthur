from django.shortcuts import render

# from project.views import PermBasedViewSet
from rest_framework import viewsets
from apps.contracts.models import Contract
from apps.contracts.serializers import ContractSerializer


# from project.permissions import

# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_url_kwarg = "client_id"

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        contracts = Contract.objects.filter(client_id=uid)
        return contracts

    # def __init__(self, *args, **kwargs):
    #     self.can_view_if_or = [CanViewClients]
    #     self.can_update_or_delete = [CanEditContract]
    #     self.can_create = [CanCreateClient]
    #     super().__init__()

    def get_permissions(self):
        return super().get_permissions()
