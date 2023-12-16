from django.db import models


class Contact(models.Model):
    # Faields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    # Methods
    def __str__(self):
        """
        String representation of the Contact object.
        This is used for display purposes in the admin & other contexts.
        """
        return self.name
