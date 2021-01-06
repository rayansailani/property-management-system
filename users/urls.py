from django.urls import path
from . import views

urlpatterns = [

    path('ownreg', views.register_owner_view, name="registerOwners"),
    path('tenreg', views.register_tenant_view, name="registerTenant"),
    path('buyreg', views.buyer_registration_view, name="registerBuyer"),
    path('ajax/load-properties/', views.load_cities, name='ajax_load_properties'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('tenant/<tenant_id>', views.tenant_detail_view, name="tenant_detail"),
    path('<tenant_id>/delete/', views.remove_tenant_view, name="remove_tenant"),
    path('send/<id>', views.message_view, name="message"),
    # path('rentreg', views.register_property_rent_view, name="rentalRegistration")
]
