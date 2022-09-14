from audioop import add
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import COUNTRIES

class Address(models.Model):
    address_line = models.CharField(_("Address"),max_length=255,blank=True,default="")
    street = models.CharField(_("Street"),max_length=255,blank=True,default="")
    city = models.CharField(_("City"),max_length=255,blank=True,default="")
    state = models.CharField(_("State"), max_length=255, blank=True, default="")
    postcode = models.CharField(_("Post/Zip-Code"),max_length=64,blank=True,default="")
    country = models.CharField(max_length=3,choices=COUNTRIES,blank=True,default="")
    
    def __str__(self) -> str:
        return self.city if self.city else ""
    
    
    def get_country_display(self):
        return self.country
    
    def get_complete_address(self):
        address = ""
        if self.address_line:
            address +=self.address_line
        if self.street:
            if address:
                address +=", " + self.street
            else:
                address +=self.street
        if self.city:
            if address:
                address +=", " + self.city
            else:
                address +=self.city
        if self.state:
            if address:
                address +=", " + self.state 
            else:
                address +=self.state
        if self.postcode:
            if address:
                address +=", " + self.postcode
            else:
                address +=self.postcode
        if self.country:
            if address:
                address +=", " + self.get_country_display()
            else:
                address +=self.get_country_display()
        return address