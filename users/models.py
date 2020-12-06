from payments.models import RentPayment
import datetime
from properties.models import PropertyForRent
from accounts.models import Account
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class Owners(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    acc_no = models.CharField(max_length=16)

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"


class Tenant(models.Model):
    property_owner = models.ForeignKey(
        Account, default=None, related_name="owner_name", on_delete=models.CASCADE)
    tenant = models.ForeignKey(
        User,  default=None, on_delete=models.CASCADE)
    property = models.ForeignKey(
        PropertyForRent, default=None, on_delete=models.CASCADE)
    aadhar_no = models.CharField(max_length=12)
    acc_no = models.CharField(max_length=16)
    ifsc_code = models.CharField(max_length=11, default='xxxxxxxxxxx')
    address_proof = models.ImageField(
        default='address_proofs/default.jpg', upload_to='address_proofs/')
    start_date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.property.property_name + " - " + self.property.floor_no + ' - ' + self.tenant.username

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"


class Buyers(models.Model):
    CHOICES = (
        ('Agent', "Agent"),
        ('Buyer', 'Buyer'),
    )
    name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    catagory = models.CharField(
        max_length=20, choices=CHOICES, default="Buyer")

    def __str__(self):
        return self.name.username + " - " + self.catagory

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"
