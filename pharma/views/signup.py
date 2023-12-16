from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from pharma.models.customer import Customer
from django.views import View


class Signup (View):
    """
    Handles user signup.

    GET:
    - Renders the signup page.

    POST:
    - Processes user signup form data.
    - Validates form data.
    - Creates a new customer if the data is valid.
    - Redirects to the store page on successful signup.
    """
    
    def get(self, request):
        # Render the signup page
        return render (request, 'pharma/signup.html')

    def post(self, request):
        # Get form data from the request 
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        # Create a new customer instance
        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        # Validate the customer data
        error_message = self.validateCustomer (customer)

        if not error_message:
            # Hash the password and register the customer
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect('pharma:store')
        else:
            # Render the signup page with an error message and the entered values
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'pharma/signup.html', data)

    def validateCustomer(self, customer):
        """
        Validates customer data.

        Returns an error message if validation fails.
        """
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
    