from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django_jalali.forms.widgets import jDateTimeInput

from phonenumber_field.widgets import RegionalPhoneNumberWidget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta(CustomUserCreationForm.Meta):
        pass


class UserUpdateForm(UserChangeForm):
    password = None

    class Meta(CustomUserCreationForm.Meta):
        fields = (
            "first_name",
            "last_name",
            "birth",
            "phone_number",
        )

        widgets = {
            "birth": jDateTimeInput(),
            "phone_number": RegionalPhoneNumberWidget(
                attrs={
                    "placeholder": "شماره تلفن",
                }
            ),
        }
