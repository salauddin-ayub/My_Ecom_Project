from django.urls import path
from . import views

app_name = 'AppOrder'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name="add"),
    path('cart/', views.cart_view, name="cart"),

]   