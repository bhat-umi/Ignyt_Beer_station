from django.urls import path
from . import views

urlpatterns=[
path("",views.orderConfirm,name="orderConfirm")
]
