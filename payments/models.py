from properties.models import PropertyForRent
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class RentPayment(models.Model):
    transaction_id = models.CharField(max_length=100)
    sender_account_no = models.CharField(max_length=16)
    sender = models.ForeignKey(
        User, related_name="sender_name", default=None, on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    rev_account_no = models.CharField(max_length=16)
    rent_amount = models.IntegerField()
    ifsc_code = models.CharField(max_length=11)
    property = models.ForeignKey(
        PropertyForRent, default=None, on_delete=models.CASCADE)
    month_of = models.IntegerField()
    rent_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + " " + self.transaction_id
