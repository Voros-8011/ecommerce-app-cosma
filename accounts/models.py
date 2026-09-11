from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class CustomUser(AbstractUser):

    Customer = 'customer'
    Vendor = 'vendor'

    Role_Choises = [
        (Customer, 'Customer'),
        (Vendor, 'Vendor')
    ]

    role = models.CharField(max_length =10, choices=Role_Choises, default=Customer)



    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
        ]
    )
    age = models.PositiveIntegerField(null=True ,blank=True)
    phone_num = models.PositiveIntegerField(validators=[MinValueValidator(1000000000, 'Phone number must be 10 digits'), MaxValueValidator(9999999999, 'Phone number must be 10 digits')] ,null=True,)
    adress = models.TextField()



