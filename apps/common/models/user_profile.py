from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from . import User
from .utils import ROLES

import time
from datetime import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(
        'Org', null=True, on_delete=models.CASCADE, blank=True, related_name="user_org")
    phone = PhoneNumberField(null=True, unique=True)
    alternate_phone = PhoneNumberField(null=True)
    address = models.ForeignKey(
        "Address", related_name="address_users", on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLES, default="USER")
    has_sales_access = models.BooleanField(default=False)
    has_marketing_access = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_organization_admin = models.BooleanField(default=False)
    date_of_joining = models.DateField(null=True, blank=True)
    activation_key = models.CharField(max_length=150, null=True, blank=True)
    key_expires = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = (("user", "org"))

    def save(self, *args, **kwargs):
        """by default the expiration time is set to 2 hours"""
        self.key_expires = timezone.now() + datetime.timedelta(hours=2)
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.is_organization_admin
