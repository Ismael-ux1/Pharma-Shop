from django.contrib import admin
from django.urls import path
from .views.home_page import Index
from .views.index import home_page

app_name = 'pharma'
urlpatterns = [
    path('index/', Index.as_view(), name='homepage'),
    path('home', home_page, name='home_page'),
]
