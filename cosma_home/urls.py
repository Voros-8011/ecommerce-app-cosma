from . import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'eccom_home'

urlpatterns = [
    path('',views.Index.as_view(),name='main'),
    path('showpro/<int:pk>',views.ShowPro.as_view(),name='showpro'),
]