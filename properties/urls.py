from django.urls import path
from . import views

urlpatterns = [
    path('rentreg', views.register_property_rent_view, name="rentalRegistration"),
    path('properties/', views.properties_for_sale_view, name="property_list"),
    path('appnt/<id>', views.appointment_view_form, name="appoint_form"),
    path('prop/<id>', views.property_detail_view, name='property_rent_detail'),
    path('salereg', views.register_property_sale_view, name="saleRegistration"),
]
