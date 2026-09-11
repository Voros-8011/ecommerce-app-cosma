from django.shortcuts import render
from products.models import Product
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Index (ListView):
    model=Product
    template_name = 'index.html'
    context_object_name = 'plist'
    # def get (self,req):
    #     pl = Product.objects.all()
    #     ctx = {'plist':pl}
    #     return render(req,'index.html',ctx)



class ShowPro ( DetailView):
    model = Product
    template_name='proshow_detail.html'


