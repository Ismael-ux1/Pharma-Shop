from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    # Fields
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    # Methods
    def makeOrder(self):
        """
        Save the order to the database.
        """
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        """
        Retrieve orders for a specific customer. Orders are ordered by date
        """
        if customer_id:
            return (Order.objects
                    .filter(customer=customer_id, status=False)
                    .order_by('-date'))
        else:
            return (Order.objects
                    .filter(customer=None, status=False)
                    .order_by('-date'))

    @staticmethod
    def get_all_orders():
        """
        Retrieve all orders. Orders are ordered by date
        """
        return Order.objects.all().order_by('-date')
