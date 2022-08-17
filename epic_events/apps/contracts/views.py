from rest_framework import viewsets
from apps.contracts.models import Contract
from apps.contracts.serializers import ContractSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from project.permissions import ContractPermissions
from user_management.models import UserModel


class ContractViewSet(viewsets.ModelViewSet):

    serializer_class = ContractSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]

    permission_classes = [ContractPermissions]

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
            return Contract.objects.filter(event__support_contact=self.request.user)
        elif self.request.user.usergroup == UserModel.UserGroup.SALE:
            return Contract.objects.filter(sales_contact=self.request.user)
        return []
