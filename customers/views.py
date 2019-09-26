from rest_framework import (status, views)
from rest_framework.response import Response
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication


class CustomersView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTTokenUserAuthentication,)

    def get(self, request):
        customers = Customer.objects.all().order_by('customerName')
        serializer = CustomerSerializer(customers, many=True)
        responseData = serializer.data
        response = Response(responseData, status=status.HTTP_200_OK)

        return response

    def post(self, request):
        requestBody = request.data

        if not(requestBody is None):
            customerSerializer = CustomerSerializer(data=requestBody)

            if(customerSerializer.is_valid()):
                customer = Customer(**requestBody)
                Customer.save(customer)
                response = Response(customerSerializer.data,
                                    status=status.HTTP_200_OK)
            else:
                response = Response(
                    'Invalid Customer Details',
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response(
                'Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
