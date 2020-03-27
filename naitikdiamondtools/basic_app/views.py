from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from . import models
# Create your views here.
class Base_class(TemplateView):
    template_name = 'homepage.html'

class ProductList(ListView):
    template_name = 'products_list.html'
    model = models.Product
    context_object_name='products'

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'products_detail.html'
    context_object_name = 'products_detail'
