from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from products.models import Product
# Create your views here.

class Order (DetailView):
    model = Product
    template_name = 'order.html'
    context_object_name = 'product'






class MainView (View):
    def get (self,req):
        return render(req,'order.html')