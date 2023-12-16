from django.shortcuts import render, redirect
from pharma.models.customer import Customer
from django.views import View
from pharma.models.product import Product
from pharma.models.order import Order


class Cart(View):
    """
    Handles the display of the shopping cart.

    GET:
    - Retrieves product IDs from the session.
    - Retrieves corresponding products.
    - Renders the cart page with the list of products.
    """
    def get(self, request):
        # Retrieve product IDs from the session cart
        ids = list(request.session.get('cart').keys())
        # Retrieve products based on the IDs
        products = Product.get_products_by_id(ids)
        # Debug: print the retrived products
        print(products)
        # Render the cart pagewith the list of products
        return render(request, 'pharma/cart.html', {'products': products})
