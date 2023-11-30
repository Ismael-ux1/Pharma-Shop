from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    email=models.EmailField()
    password = models.CharField(max_length=200)

    def register(self):
        self.save()

    def __str__(self):
        return self.name

    @staticmethod
    def get_customer_by_email(email):
        user = User.objects.get(email=email)
        return Customer.objects.get(user=user)
