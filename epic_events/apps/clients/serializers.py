from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [ 'id',
        'first_name',
        'last_name',
        'email',
        'company_name',
        'phone',
        'sales_contact',
        ]
    sales_contact = serializers.SerializerMethodField('get_sales_contact_mail')

    def get_sales_contact_mail(self, obj):
        if obj.sales_contact is None:
            return "Not attributed yet"
        return obj.sales_contact.email

