from django.contrib import admin
from users.models import Owners, PropertyForRent, Tenant, Buyers
# Register your models here.

admin.site.register(Owners)
# admin.site.register(PropertyForRent)
admin.site.register(Tenant)
admin.site.register(Buyers)
