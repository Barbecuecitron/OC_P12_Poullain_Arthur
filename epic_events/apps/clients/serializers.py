from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [ 'first_name',
        'last_name',
        'email',
        'company_name',
        'phone'
        ]
