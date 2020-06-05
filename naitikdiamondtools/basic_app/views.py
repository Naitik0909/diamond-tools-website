from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, View
from . import models
from django.contrib import messages
from django.core.mail import send_mail
import os
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
            sendMail(email, query)
        else:
            phone = form.get('email-phone')
            new_query = models.QueryBox.objects.create(
            phone = phone,
            query = query
            )
            sendMail(phone, query)
        new_query.save()

def sendMail(user_data, user_query):
    self_message = '''Just received a new query from a customer.

            Customer credentials:
            '''+str(user_data)+'''

            Customer query:
            '''+user_query

    send_mail(
    'New enquiry received for Naitik Diamond Tools!',
    self_message,
    os.environ['SEND_FROM_EMAIL'],
    ['parmarnaitik0909@gmail.com', 'naitikdiamondtools@yahoo.com']
    )


class BaseClass(View):
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        context = {'products': products}
        return render(request, "homepage.html", context=context)
    def post(self, request, *args, **kwargs):
        formSubmitted(self, request, *args, **kwargs)
        return redirect("index") # also return a message that message has been sent

class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutus.html')

class ProductDetail(View):
    def get(self, request, *args, **kwargs):
        path = self.request.path   # 127.0.0.1:8000/<path>
        products_list = ["/1/", "/2/", "/3/", "/4/", "/5/"]

        # For single blade's table
        total = []
        for i in range(0, 11):
            total.append(i)
        sizes_available = [1000, 1200, 1300, 1400, 1600, 1700, 1800, 1800, 2000, 2500, 3000]
        segments = [70,80,88,104,108,112,120,120,128,140,160]
        dimension = ['24*7.4*15', '24*8.4*15','24*8.5*15/20','24*9.0*15/20','24*9.8*15/20'
            ,'24*9.8*15'
            ,'24*9.8*15'
            ,'24*10.20*15/20'
            ,'24*10.5*15'
            ,'24*11.5*15'
            ,'24*12.5*15']
        multi_dimension = [
                    '23*6.5*15/20',
                    '23*7.4*15/20',
                    '23*8.5*15/20',
                    '23*9.0*15/20',
                    '24*6.5*15/20',
                    '24*7.4*15/20',
                    '24*8.5*15/20',
                    '24*9.0*15/20'
                    ]
        for i in range(0, 5):
            if (path == products_list[i]):
                product_detail = models.Product.objects.get(id=i+1)
                context = {
                    'product_detail':product_detail,
                    'sizes_available':sizes_available,
                    'segments':segments,
                    'dimension':dimension,
                    'total':total,
                    'multi_dimension':multi_dimension,
                    'env':os.environ.get('SENDGRID_API_KEY')
                }
                return render(request, "products_detail.html", context=context)
    def post(self, request, *args, **kwargs):
        formSubmitted(self, request, *args, **kwargs)
        messages.success(request, "Your query has been sent to us successfully! We will revert back to you soon.")
        return redirect("index")
