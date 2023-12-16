from django.db import models


class Customer(models.Model):
    # Fields
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def register(self):
        """
        Register a customer by saving thier object to the database
        """
        self.save()

    def __str__(self):
        """
        String representation of the Customer object.
        This is used for display in the admin & other contexts.
        """
        return f'{self.first_name} {self.last_name}'

    def isExists(self):
        """
        Check if a customer with given email already exists.
        Returns True if exists, else False.
        """
        return Customer.objects.filter(email=self.email).exists()

    @staticmethod
    def get_customer_by_email(email):
        """
        Retrive a customer by thier email address.
        Returns the customer oject if found, else None.
        """
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None
