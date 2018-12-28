from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


from products.models import Product
# Create your models here.

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="has_cart")
    products = models.ManyToManyField(Product)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.id)



