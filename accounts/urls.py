from . import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('',views.Sign_Up_View.as_view() ,name='sign_up'),
    path('vendor/register/', views.VendorRegistrationView.as_view(), name='vendor_register'),
    path('vendor/login/', views.VendorLoginView.as_view(), name='vendor_login'),
]