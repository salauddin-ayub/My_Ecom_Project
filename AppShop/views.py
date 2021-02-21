from django.shortcuts import render

# Import views for
from django.views.generic import ListView, DetailView

# Model 
from AppShop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    model = Product
    template_name = "home.html"

class ProductDetail (LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'   

