# Generated by Django 5.0.7 on 2024-07-17 12:03

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birth",
            field=django_jalali.db.models.jDateField(),
            preserve_default=False,
        ),
    ]
