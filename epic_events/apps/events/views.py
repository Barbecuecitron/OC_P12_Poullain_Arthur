from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import EventSerializer
from .models import Event
from project.permissions import EventPermissions, IsManagement
from user_management.models import UserModel
from apps.contracts.models import Contract
# from clients.models import Client

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [EventPermissions | IsManagement ]

    """ Sales team : can CREATE new events DONE
                     can VIEW events of their own clients
                     can UPDATE events of their own clients if not finished
        Support team : can VIEW events they are assigned to
                       can UPDATE events of their own clients if not finished
    """

    def get_queryset(self):
        if self.request.user.usergroup == UserModel.UserGroup.SALE:
            return Event.objects.filter(contract__sales_contact=self.request.user)

        elif self.request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return Event.objects.filter(support_contact=self.request.user)

        elif self.request.user.usergroup == UserModel.UserGroup.MANAGEMENT:
            return Event.objects.all()