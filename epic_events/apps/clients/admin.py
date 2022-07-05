from django.contrib import admin

# Register your models here.
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ("company_name", "sales_contact", "first_name", "last_name")
    list_filter = ("sales_contact",)


admin.site.register(Client, ClientAdmin)
