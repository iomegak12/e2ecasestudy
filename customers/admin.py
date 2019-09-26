from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'customerId',
        'customerName', 'address',
        'credit', 'status', 'remarks'
    ]


admin.site.register(Customer, CustomerAdmin)
