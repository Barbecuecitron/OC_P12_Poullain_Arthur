from django.contrib import admin
from .models import Contract
# Register your models here.
# class ContractAdmin(admin.ModelAdmin):
#     list_display= ("company_name","sales_contact", "first_name","last_name")

admin.site.register(Contract)#, ContractAdmin)