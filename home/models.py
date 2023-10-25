from django.db import models

# Create your models here.

COLOR_CHOICES = ( 
    ("White", "White"), 
    ("Black", "Black"), 
    ("Red", "Red"), 
    ("Blue", "Blue"), 
    ("Green", "Green"),
) 

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=20)
    description = models.TextField()
    mrp = models.IntegerField()
    color = models.CharField( 
        max_length = 20, 
        choices = COLOR_CHOICES, 
        default = 'Red'
        )