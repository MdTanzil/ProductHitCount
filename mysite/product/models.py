from django.db import models

# Create your models here.

class Product(models.Model):
    """Model definition for Product."""

    userId = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    body = models.TextField()


    def __str__(self):
        """Unicode representation of Product."""
        return self.title
