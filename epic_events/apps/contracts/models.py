from django.db import models
from apps.clients.models import Client
from user_management.models import UserModel
from datetime import datetime


class Contract(models.Model):
    client = models.ForeignKey(
        to=Client,
        blank=False,
        on_delete=models.CASCADE,
    )

    sales_contact = models.ForeignKey(
        to=UserModel,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"usergroup": "Sale"},
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    STATUS = (("OPEN", "Open"), ("SIGNED", "Contract Signed"), ("ENDED", "Ended"))

    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default="OPEN",
    )

    def __str__(self):
        prettified_payment = str(self.payment_due).split(" ")[0]
        display_name = f"{self.client} - {prettified_payment}"
        return display_name
