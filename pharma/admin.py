from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.product import Product
from .models.contact import Contact


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contact)
