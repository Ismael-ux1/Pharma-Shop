from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.views import View
from pharma.models.product import Product
from pharma.models.category import Category


# Index class inherits from Django's View class
class Index(View):
    # Handles POST requests
    def post(self, request):
        # Get product and remove flag from the POST data
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        # Get the cart from the session, defaulting to an empty dictionary
        # if it doesn't exist
        cart = request.session.get('cart', {})

        # Update the quantity of the product in the cart
        cart[product] = self.update_cart_quantity(cart, product, remove)

        # Update the session cart
        request.session['cart'] = cart

        print('cart', request.session['cart'])
        return HttpResponseRedirect(reverse('pharma:store'))

    # Handles GET requests
    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

    # Static method to update the quantity of a product in the cart
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('pharma:store')


# Function to handle the store view

def store(request):
    # Ensure the session has a cart, even if it's empty
    request.session.setdefault('cart', {})

    # Get the category ID from the GET parameters
    categoryID = request.GET.get('category')

    # Get the products for the given category,
    # or all products if no category is specified
    products = Product.get_products_by_category(categoryID) if categoryID else Product.objects.all()

    # Get all categories
    categories = Category.objects.all()

    # Prepare the data for the template
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'pharma/index.html', data)
