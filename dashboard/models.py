from django.db import models
from landing.models import User

def getDetailsFromUID(id):
    obj = User.objects.get(id=id)
    return obj

# Create your models here.
class Produce(models.Model):
    farmerid = models.IntegerField(default=0)

    # Product details
    name = models.CharField(max_length=255, help_text="Product name")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit")
    
    # Quantity and unit of measurement
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Available quantity")
    unit = models.CharField(max_length=50, help_text="Unit of measurement")

    # Date and time of listing
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def user(self):
        return getDetailsFromUID(self.farmerid)