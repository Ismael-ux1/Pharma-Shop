# test_category.py
from django.test import TestCase
from pharma.models.category import Category


class CatagoryModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category', description='Test Description')

    def test_category_name_label(self):
        # Test the label of the name field
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_category_name_max_length(self):
        # Test the max length of the name field
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_categoy_str_representation(self):
        # Test the string representation of the category object
        category = Category.objects.get(id=1)
        self.assertEquals(str(category), 'Test Category')