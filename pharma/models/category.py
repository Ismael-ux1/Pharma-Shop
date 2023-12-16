from django.db import models


class Category(models.Model):
    # Fields
    name = models.CharField(max_length=200)

    # Methods
    def __str__(self):
        """
        String representation of the Catagory object.
        This is used for display in the admin & other contexts.
        """
        return self.name

    @staticmethod
    def get_categories():
        """
        Returns all categories.
        A static method is used for simplicity,
        """
        return Category.objects.all()
