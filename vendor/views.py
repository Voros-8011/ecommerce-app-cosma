from django.shortcuts import render
from django.views import View
from products.models import Product
from vendor.owner import Owner_Create_View,Owner_Delet_View,Owner_Detail_view,Owner_List_view,Owner_Update_View
# Create your views here.



class Vendor_Detail (Owner_Detail_view):
    model = Product
    template_name='vendor_detail.html'


class Vendor_creat_view (Owner_Create_View):
    model = Product
    template_name='vendor_form.html'
    fields=['prod_name','prod_img','prod_desc','prod_qunt','prod_price']




class Vendor_update_view (Owner_Update_View):
    model = Product
    template_name='vendor_form.html'
    fields=['prod_name','prod_img','prod_desc','prod_qunt','prod_price']

            



class Vendor_delete_view (Owner_Delet_View):
    model = Product
    template_name='vendor_delet.html'





class Vendor_main (Owner_List_view):
    model = Product
    template_name='vendor_list.html'
    context_object_name = 'vendor_list'

    