from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    patronym = models.CharField(max_length=120, blank=True, default="")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True, default="")

    #permissions
    can_add_data = models.BooleanField(default=False)
    can_create_user = models.BooleanField(default=False)
    can_add_threshold = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    #organization to belong
    position = models.ForeignKey(
        "Position", on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    department = models.ForeignKey(
        "Department", on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)


class Organization(models.Model):
    name = models.CharField(max_length=255)

    city = models.CharField(max_length=51)
    district = models.CharField(max_length=51)
    street = models.CharField(max_length=51)
    building_number = models.CharField(max_length=51)
    contact_phone = models.CharField(max_length=51)
    contact_email = models.CharField(max_length=51)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='positions')

    def __str__(self):
        return self.name
