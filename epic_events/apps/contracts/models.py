from django.db import models
from apps.clients.models import Client
from user_management.models import User_Model
from datetime import datetime


# Create your models here.

class Contract(models.Model):
    client = models.ForeignKey(
        to = Client, 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        #limit_choices_to={"usergroup": "Sale"},
        )

    sales_contact = models.ForeignKey(
        to = User_Model, 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"usergroup": "Sale"},
        )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField(default=0.0)
    payment_due = models.DateTimeField(default=datetime.now())

    def __str__(self):
        prettified_payment = str(self.payment_due).split(" ")[0]
        display_name = f"{self.client} - {prettified_payment}"
        return display_name



class Status(models.Model):
    
    contract = models.ForeignKey(
        to = Client, 
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    STATUS = (
        ('OPEN', 'Open'),
        ('SIGNED', 'Contract Signed')
    )

