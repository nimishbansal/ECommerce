from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from carts.models import Cart

User=get_user_model()


def post_save_user_receiver(sender,instance,created,*args,**kwargs):
    if created:
        new_cart=Cart.objects.create(user=instance)


post_save.connect(post_save_user_receiver,sender=User)
