from django.shortcuts import render
from project.views import PermBasedViewSet
from .models import Client 
from .serializers import ClientSerializer
from project.views import PermBasedViewSet
from project.permissions import IsSale, IsSupport, CanViewClients, CanEditClient

# Create your views here.

class ClientViewSet(PermBasedViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def __init__(self, *args, **kwargs):
        self.can_view_if_or = [CanViewClients]
        self.can_cud_if_or = [CanEditClient]
        super().__init__()

    def get_permissions(self):
        return super().get_permissions()


    