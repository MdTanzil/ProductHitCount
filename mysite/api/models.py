from django.db import models

# Create your models here.
class ProductViewCounter(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    view_counter = models.IntegerField(default=0)
    def __str__(self):
        """Unicode representation of MODELNAME."""
        self.name


class View_time(models.Model):
    """Model definition for Deating."""

    product_id = models.ForeignKey(ProductViewCounter, on_delete=models.CASCADE)
    View_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Unicode representation of Deating."""
        pass
