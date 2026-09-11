from . import views
from django.urls import path,reverse_lazy
from django.views.generic import TemplateView

app_name = 'vendor'

urlpatterns = [
    path('',views.Vendor_main.as_view(),name='all'),
    path('vendor/<int:pk>',views.Vendor_Detail.as_view(),name='vendor_detail'),
    path('vendor/creat',views.Vendor_creat_view.as_view(success_url =reverse_lazy('vendor:all')),name='vendor_creat'),
    path('vendor/update/<int:pk>',views.Vendor_update_view.as_view(success_url =reverse_lazy('vendor:all')),name='vendor_update'),
    path('vendor/delete/<int:pk>',views.Vendor_delete_view.as_view(success_url =reverse_lazy('vendor:all')),name='vendor_delete')
]