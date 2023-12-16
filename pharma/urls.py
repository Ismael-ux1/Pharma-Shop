from django.contrib import admin
from django.urls import path
from pharma.views.landing_page import LandingPageView
from .views.index import Index , store
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.signup import Signup
from .views.login import Login , logout
from pharma.views.contact import contact, success

app_name = 'pharma'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('index/', Index.as_view(), name='index'),
    path('store/', store, name='store'),
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', CheckOut.as_view(), name='checkout'),
    path('orders/all/', OrderView.as_view(), name='all_orders'),
    path('orders/', OrderView.as_view()),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout , name='logout'),
    path('contact.html/', contact, name='contact'),
    path('success/', success, name='success'),
]