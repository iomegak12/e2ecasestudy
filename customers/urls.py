from django.conf.urls import url
from customers.views import CustomersView

urlpatterns = [
    url(r'customers', CustomersView.as_view(), name='customers_all')
]
