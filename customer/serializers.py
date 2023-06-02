from rest_framework import serializers
from customer.models import *

class GetCustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields ="__all__"


class GetCustomerAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields ="__all__"

   
class CustomerDetailsAddressSerializers(serializers.ModelSerializer):
    customer_address = GetCustomerAddressSerializers(many=True)
    
    class Meta:
        model = Customers
        fields = ('first_name','last_name','mobile','age','country_name','city_name','dob','pincode')

        
