from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta(CustomUserCreationForm.Meta):
        pass


class UserUpdateForm(forms.ModelForm):
    class Meta(CustomUserCreationForm.Meta):
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "birth",
            "phone_number",
        )
