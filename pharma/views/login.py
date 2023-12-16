from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from pharma.models.customer import Customer
from django.views import View


class Login(View):
    """
    Handles user login.

    GET:
    - Renders the login page.

    POST:
    - Validates user credentials.
    - Logs in the user if valid.
    - Redirects to the specified return URL or the store page.
    """
    return_url = None

    def get(self, request):
        # Store the return URL from the query parameters
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'pharma/login.html')

    def post(self, request):
        # Get user credentials from the form
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        # Retrieve the customer based on the provided email
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            # Check if the password is valid
            flag = check_password (password, customer.password)
            if flag:
                # Log in the user and set the customer ID in the session
                request.session['customer'] = customer.id

                # Redirect to the return URL or the store page
                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('pharma:store')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'pharma/login.html', {'error': error_message})

def logout(request):
    """
    Logs out the user by clearing the session.
    Redirects to the login page after logout.
    """
    request.session.clear()
    return redirect('pharma:login')
