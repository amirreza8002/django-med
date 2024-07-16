from django.contrib.auth.models import AbstractUser

from django_jalali.db import models as jmodels

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    birth = jmodels.jDateField
    phone_number = PhoneNumberField(blank=True, null=True)

    objects = jmodels.jManager()
