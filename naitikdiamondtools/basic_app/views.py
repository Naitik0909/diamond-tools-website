from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, View
from . import models
# Create your views here.
class Base_class(View):
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        context = {'products': products}
        return render(request, "homepage.html", context=context)

class ProductList(ListView):
    template_name = 'products_list.html'
    model = models.Product
    context_object_name='products'

class ProductDetail(DetailView):
    model = models.Product
    template_name = 'products_detail.html'
    context_object_name = 'products_detail'
