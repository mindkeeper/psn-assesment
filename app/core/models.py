from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,)


class CustomerManager(BaseUserManager):

    def create_customer(self, email, phone_number, name, password,
                        **extra_fields):
        customer = self.model(
            email=email,
            phone_number=phone_number,
            name=name,
            **extra_fields)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer


class Customer(AbstractBaseUser, PermissionsMixin):
    MALE = "male"
    FEMALE = "female"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    email = models.EmailField(max_length=255, unique=True)
    title = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    image = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomerManager()
    USERNAME_FIELD = "email"

