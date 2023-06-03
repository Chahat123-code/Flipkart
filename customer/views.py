from django.shortcuts import render
from customer.models import *
from customer.serializers import *

# Create your views here.

from rest_framework import status
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework .permissions import AllowAny, IsAuthenticated

class GetCustomerView(APIView):
    def get(self,request):
        instance =Customers.objects.all()
        serializers = GetCustomerSerializers(instance,many=True)
        return Response(serializers.data)

    def post(self,request):
       params = request.data
       print("data-",params)
       serializers = GetCustomerSerializers(data=params)
       serializers.is_valid(raise_exception = True)
       serializers.save()
       return Response({"Message:","Save Successfully" })

class GetCustomerAddress(APIView):
    def get(self,request):
        instance = CustomerAddress.objects.all()
        serializers = GetCustomerAddressSerializers(instance,many=True)
        return Response(serializers.data)
    

class CustomerDetailsAddressView(APIView):
    def get (self,request,pk):
      instance = Customers.objects.filter(id = pk)
      ser =CustomerDetailsAddressSerializers(instance,many=True)
      return Response(ser.data)

