from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contract
from apps.contracts.serializers import ContractSerializer
from apps.events.models import Event
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from project.permissions import ContractPermissions, IsManagement
from rest_framework.permissions import IsAuthenticated
from user_management.models import UserModel
import logging
logger = logging.getLogger('django')

# Return contracts linked to events we are responsible for
def get_support_related_contracts(user):
    support_contracts = []
    for event in Event.objects.filter(support_contact = user):
        if event.support_contact == user and event.contract:
            # logger.info(f"{event.contract.id}")
            support_contracts.append(event.contract.id)
    return Contract.objects.filter(id__in=support_contracts)

class ContractViewSet(viewsets.ModelViewSet):

    serializer_class = ContractSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]

    permission_classes = [IsAuthenticated, IsManagement | ContractPermissions]

    search_fields = [
        "^client__first_name",
        "^client__last_name",
        "^client__email",
        "^client__company_name",
    ]
    
    filterset_fields = {
        "date_created": ["gte", "lte"],
        "payment_due": ["gte", "lte"],
        "amount": ["gte", "lte"],
        "status": ["exact"],
    }

    def get_queryset(self):
        if self.request.user.usergroup == UserModel.UserGroup.SUPPORT:
            return get_support_related_contracts(self.request.user)
       
        elif self.request.user.usergroup == UserModel.UserGroup.SALE:
            return Contract.objects.filter(client__sales_contact=self.request.user)

        return Contract.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(obj).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(sales_contact=self.request.user)
