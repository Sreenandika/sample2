from django.urls import path
from .views import home, about ,contact, productadd, product_list, product_view

urlpatterns = [
    path('',home, name='home'),
    path('productlist/',product_list, name='product-list'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('productadd/',productadd, name='productadd'),
    path('productview/<int:product_id>/view/',product_view,name='product_view')
]