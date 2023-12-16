from django.db import models
from .category import Category


class Product(models.Model):
    # Fields
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='',
                                   blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    # Methods
    def __str__(self):
        """
        String represntation of the Product object.
        """
        return self.name

    @staticmethod
    def get_products_by_category(category_id):
        """
        Retrive products for a specific category.
        """
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        """
        Retrive products by a list of IDs.
        """
        return Product.objects.filter (id__in=ids)
    
    
    @staticmethod
    def get_all_products():
        """
        Retrive all products.
        """
        return Product.objects.all()