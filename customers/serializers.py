from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customerId', 'customerName',
            'address', 'credit', 'status', 'remarks'
        ]