from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,)


class CustomerManager(BaseUserManager):

    def create_customer(self, email, name, password,
                        **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        customer = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer

    def create_admin(self, email, password, **extra_fields):
        admin = self.create_customer(email, "admin", password)
        admin.is_superuser = True
        admin.set_password(password)
        admin.save(using=self._db)
        return admin


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
    phone_number = models.CharField(max_length=20, unique=True, blank=True,
                                    null=True)
    image = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomerManager()
    USERNAME_FIELD = "email"
