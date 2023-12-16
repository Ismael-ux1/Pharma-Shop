from django.shortcuts import render, redirect
from pharma.models.customer import Customer
from django.views import View
from pharma.models.product import Product
from pharma.models.order import Order


class CheckOut(View):
    """
    Handles the checkout process.

    POST:
    - Retrieves address, phone, customer ID, and cart data from the request.
    - Retrieves products based on the IDs in the cart.
    - Creates an anonymous customer if no logged-in customer.
    - Creates orders for each product in the cart.
    - Clears the cart in the session.
    - Redirects to the cart page.
    """

    def post(self, request):
        # Retrieve address, phone, customer ID, and cart data from the request
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')

        # Retrieve products based on the IDs in the cart
        products = Product.get_products_by_id(list(cart.keys()))

        # Debug: print the retrieved data
        print(address, phone, customer_id, cart, products)

        # If there's no logged-in customer, create an anonymous customer
        if customer_id is None or not Customer.objects.filter(id=customer_id).exists():
            customer = Customer.objects.create(first_name='Anonymous', email='anonymous@example.com')
        else:
            customer = Customer.objects.get(id=customer_id)

        # Create orders for each product in the cart
        for product in products:
            print(cart.get(str(product.id)))
            order = Order.objects.create(customer=customer,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        
        # Clear the cart in the session
        request.session['cart'] = {}

        # Redirect to the cart page
        return redirect('pharma:cart')
