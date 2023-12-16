from django.shortcuts import render, redirect
from pharma.models.customer import Customer
from django.views import View
from pharma.models.product import Product
from pharma.models.order import Order

class OrderView(View):
    """
    Handles the display of orders.

    GET:
    - Retrieves the customer ID from the session.
    - Fetches orders based on the customer ID for logged-in users.
    - Fetches all orders for anonymous users.
    - Renders the orders page with the list of orders.
    """
    
    
    def get(self, request):
        # Retrieve the customer ID from the session
        customer = request.session.get('customer')
        
        if customer:
            # Fetch orders for logged-in users
            orders = Order.get_orders_by_customer(customer)
        else:
            # Fetch orders for anonymous users (you may customize this logic)
            orders = Order.get_all_orders()

        # Debug: print the retrieved orders
        print("Orders:", orders)

        # Render the orders page with the list of orders
        return render(request, 'pharma/orders.html', {'orders': orders})
