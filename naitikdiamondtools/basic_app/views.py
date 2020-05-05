from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, View
from . import models
# Create your views here.

def formSubmitted(self, request, *args, **kwargs):
    if request.method == "POST":
        form = request.POST
        phone = 0
        email = ''
        query = form.get('actual-query')
        if '@' in form.get('email-phone'):
            email = form.get('email-phone')
            new_query = models.QueryBox.objects.create(
            email = email,
            query = query
            )
        else:
            phone = form.get('email-phone')
            new_query = models.QueryBox.objects.create(
            phone = phone,
            query = query
            )
        new_query.save()


class BaseClass(View):
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        context = {'products': products}
        return render(request, "homepage.html", context=context)
    def post(self, request, *args, **kwargs):
        formSubmitted(self, request, *args, **kwargs)
        return redirect("index") # also return a message that message has been sent

class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        path = self.request.path
        products_list = ["/1/", "/2/", "/3/", "/4/", "/5/"]
        for i in range(0, 5):
            if (path == products_list[i]):
                product_detail = models.Product.objects.get(id=i+1)
                context = {
                    'product_detail':product_detail,
                }
                return render(request, "products_detail.html", context=context)
    def post(self, request, *args, **kwargs):
        formSubmitted(self, request, *args, **kwargs)
        return redirect("index")
