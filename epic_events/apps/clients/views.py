from django.shortcuts import render
from project.views import PermBasedViewSet
from .models import Client 
from .serializers import ClientSerializer
from project.views import PermBasedViewSet
from project.permissions import IsSale, IsSupport, CanViewClients, CanEditClient, CanCreateClient

# Create your views here.

class ClientViewSet(PermBasedViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def __init__(self, *args, **kwargs):
        self.can_view_if_or = [CanViewClients]
        self.can_update_or_delete = [CanEditClient]
        self.can_create = [CanCreateClient]
        super().__init__()

    def get_permissions(self):
        return super().get_permissions()


    