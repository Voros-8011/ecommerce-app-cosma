from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Product (models.Model):
    prod_name = models.CharField(max_length=200)
    prod_img = models.ImageField(upload_to='product_images/')
    prod_desc = models.TextField()
    prod_qunt = models.IntegerField()
    prod_price = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.prod_name
    

