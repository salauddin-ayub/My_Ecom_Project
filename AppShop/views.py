from django.shortcuts import render

# Import views for
from django.views.generic import ListView, DetailView

# Model 
from AppShop.models import Product

# Create your views here.

class Home(ListView):
    model = Product
    template_name = "home.html"

