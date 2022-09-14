from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import time
import arrow
from phonenumber_field.modelfields import PhoneNumberField

from . import ROLES


def img_url(self, filename):
    hash_ = int(time.time())
    return "%s%s%s" % ("profile_pics", hash_, filename)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=150, unique=True)
    alternate_email = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(("date joined"), auto_now_add=True)
    profile_pic = models.FileField(
        max_length=1000, upload_to=img_url, null=True, blank=True)
    skype_ID = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    @property
    def get_short_name(self):
        return self.username

    @property
    def documents(self):
        return self.document_uploaded.all()

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    @property
    def created_on_arrow(self):
        return arrow.get(self.date_joined).humanize()

    class Meta:
        ordering = ["-is_active"]

    def __str__(self) -> str:
        return self.email


