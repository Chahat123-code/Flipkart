from django.contrib import admin
from django.urls import path,include
from customer.views import *
urlpatterns = [
    path('get-cusomers',GetCustomerView.as_view()),
     path('get-cusomeraddress',GetCustomerAddress.as_view()),

  
]
