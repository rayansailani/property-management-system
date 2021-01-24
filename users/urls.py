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
    path('maintain/<id>', views.maintainers_view, name="maintainer_info"),
    path('remove/maintainer/<id>', views.remove_maintainer_view,
         name="remove_maintainer"),
    path('remove/rent_ppty/<id>', views.remove_rent_listing_view,
         name="remove_rental_property"),
    path('remove/sale_ppty/<id>', views.remove_sale_listing_view,
         name="remove_sale_property"),
    # path('rentreg', views.register_property_rent_view, name="rentalRegistration")
]
