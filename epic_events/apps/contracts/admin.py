from django.contrib import admin
from .models import Contract
# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    
    list_display = ("contract_info","sales_contact")
    def contract_info(self, obj):
        return obj

admin.site.register(Contract, ContractAdmin)