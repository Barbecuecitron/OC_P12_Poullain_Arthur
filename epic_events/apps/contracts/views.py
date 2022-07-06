from rest_framework import viewsets
from apps.contracts.models import Contract
from apps.contracts.serializers import ContractSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ContractViewSet(viewsets.ModelViewSet):

    serializer_class = ContractSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
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
        contracts = Contract.objects.all()

        # uid = self.kwargs.get(self.lookup_url_kwarg)
        # contracts = Contract.objects.filter(client_id=uid)
        # contracts = Contract.objects.filter()
        return contracts

    def get_permissions(self):
        return super().get_permissions()
