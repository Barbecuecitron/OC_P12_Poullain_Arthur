from django.db import models
from apps.contracts.models import Contract
from project import settings
from user_management.models import UserModel

# Create your models here.
class Event(models.Model):
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        limit_choices_to={"status": "OPEN"},
        related_name="event",
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"usergroup": UserModel.UserGroup.SUPPORT},
    )
    event_status = models.BooleanField(default=False, verbose_name="Completed")
    attendees = models.PositiveIntegerField(default=1)
    event_date = models.DateTimeField(blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        name = f"{self.contract.client.last_name} {self.contract.client.first_name}"
        date = self.event_date.strftime("%Y-%m-%d")
        if self.event_status is False:
            event_state = "TO HAPPEN"
        else:
            event_state = "DONE"

        return f"Event #{self.id} : {name} | Date : {date} | ({event_state})"
