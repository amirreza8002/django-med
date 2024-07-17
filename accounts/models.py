from django.contrib.auth.models import AbstractUser, UserManager

from django_jalali.db import models as jmodels

from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager, jmodels.jManager):
    pass


class CustomUser(AbstractUser):
    birth = jmodels.jDateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    objects = CustomUserManager()
