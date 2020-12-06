from django.contrib import admin
from . models import PropertyForRent, PropertyForSale, Appointment
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(PropertyForRent)
admin.site.register(PropertyForSale)
admin.site.register(Appointment)
