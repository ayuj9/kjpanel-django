from django.db import models

# Create your models here.
class Names(models.Model):
    id = models.IntegerField(primary_key =True)
    name = models.CharField(max_length = 150)
    recipieLink = models.URLField(max_length=200 , null = True , blank =True)


class ProductImage(models.Model):
    product = models.ForeignKey(Names , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='autoS/images')