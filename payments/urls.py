from django.urls import path
from . import views

urlpatterns = [
    path('rent', views.payment_view, name='payment_rent'),
]
