from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
      
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    body = models.TextField()
    view_counter = models.IntegerField(default=0)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

class ProductViewCounter(models.Model):
    """Product view count ."""

    # TODO: Define fields here
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    View_time = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        self.product_id

