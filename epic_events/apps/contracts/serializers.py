from .models import Contract
from rest_framework import serializers

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [ 'id',
        'clean_name',
        'status',
        'sales_contact',
        'date_created',
        'date_updated',
        'amount',
        'payment_due',
        ]

    sales_contact = serializers.SerializerMethodField('get_sales_contact_mail')
    clean_name = serializers.SerializerMethodField('get_clean_name')

    def get_clean_name(self, obj):
        prettified_payment = str(obj.payment_due).split(" ")[0]
        display_name = f"{obj.client} - {prettified_payment}"
        return display_name

    def get_sales_contact_mail(self, obj):
        if obj.sales_contact is None:
            return "Not attributed yet"
        return obj.sales_contact.email

