from django.contrib import admin
from . models import PropertyForRent, PropertyForSale, Appointment, visit
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(PropertyForRent)
admin.site.register(PropertyForSale)
admin.site.register(Appointment)
admin.site.register(visit)
