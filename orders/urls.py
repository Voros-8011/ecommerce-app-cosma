from . import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'orders'

urlpatterns = [
    path('',views.MainView.as_view(),name='order_pa'),
    path('order/<int:pk>',views.Order.as_view(),name='order'),
]