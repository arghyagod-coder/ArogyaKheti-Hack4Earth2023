from django.db import models
from .login_cfg import GetAddressDetails, GetCoordinates
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.
class User(models.Model):
    fidc = models.UUIDField(default=uuid.uuid4().int, unique=True)
    name = models.CharField(max_length=200)
    phone = PhoneNumberField(null=False, default="None", blank=False, unique=True, region='IN')
    pincode = models.IntegerField()
    # district, state, country = GetAddressDetails(pincode)
    # lat,lon = GetCoordinates(pincode)
    farmname = models.CharField(max_length=200)
    farmlandmarks = models.CharField(blank=True, max_length=200)
    farmarea = models.DecimalField(max_digits=10000, decimal_places=3)
    address = models.TextField(blank=True,max_length=700)
    bio = models.TextField(blank=True,max_length=700)

    @property 
    def addressinfo(self):
        state, country = GetAddressDetails(self.pincode)
        return [state, country]

    @property 
    def coords(self):
        lat ,lon = GetCoordinates(self.pincode)
        return [lat, lon]
    

