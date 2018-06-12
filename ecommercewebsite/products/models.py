from django.db import models


from .utils import unique_slug_generator
# Create your models here.
import sys,os

from tags.models import Tag


from django.db.models.signals import pre_save

def product_directory_path(instance, filename):
    return 'products/{0}.{1}'.format(instance.title,filename.split(".")[1])


class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

    def featured(self):
        return self.get_queryset().filter(featured=True)


class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    slug=models.SlugField(blank=True,unique=True)
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(max_digits=20,decimal_places=2)
    image=models.ImageField(upload_to=product_directory_path,blank=True,null=True)
    active=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tagged")


    objects=ProductManager()

    def get_image_url(self):
        print("getting url")
        if self.image:
            return self.image.url
        else:
            return ""
    def __str__(self):
        return self.title




def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)