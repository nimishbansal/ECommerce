from django.db import models

# Create your models here.

def product_directory_path(instance, filename):
    return 'products/{0}.{1}'.format(instance.title,filename.split(".")[1])



class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(max_digits=20,decimal_places=2)
    image=models.ImageField(upload_to=product_directory_path,blank=True,null=True)

    def get_image_url(self):
        print("getting url")
        return self.image.url

    def __str__(self):
        return self.title
