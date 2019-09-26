from django.test import TestCase
from django.urls import reverse
from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework.test import APIClient


class BaseCustomersAPITest(TestCase):
    client = APIClient()

    @staticmethod
    def create(id, name, address, credit, status, remarks):
        if not(name is None) and not(address is None):
            Customer.objects.create(customerId=id,
                                    customerName=name,
                                    address=address,
                                    credit=credit,
                                    status=status,
                                    remarks=remarks)

    def setUp(self):
        self.create('C100011', 'Northwind Traders',
                    'Bangalore', 12000, True, 'Simple Record')
        self.create('C100012', 'Eastwind Traders',
                    'Bangalore', 12000, True, 'Simple Record')
        self.create('C100013', 'Southwind Traders',
                    'Bangalore', 12000, True, 'Simple Record')
        self.create('C100014', 'Westwind Traders',
                    'Bangalore', 12000, True, 'Simple Record')
        self.create('C100015', 'Oxyrich Traders',
                    'Bangalore', 12000, True, 'Simple Record')


class GetAllCustomersTest(BaseCustomersAPITest):
    def test_all_customers(self):
        response = self.client.get(reverse('customers_all'))
        expectedCustomers = Customer.objects.all().order_by('customerName')
        serializer = CustomerSerializer(expectedCustomers, many=True)

        expectedCustomersData = serializer.data
        actualCustomersData = response.data

        expectedStatusCode = 200
        actualStatusCode = response.status_code

        self.assertEqual(expectedStatusCode, actualStatusCode)
        self.assertEqual(expectedCustomersData, actualCustomersData)
