from django import forms as d_forms
from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User, Creator, Consumer


class UserChangeForm(UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_username": _(
                "This username has already been taken."
            )
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )
        


class RegisterForm(d_forms.ModelForm):

    email = d_forms.EmailField()

    class Meta:
        model = Consumer
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar']

class CreatorRegister(d_forms.ModelForm):

    email = d_forms.EmailField()

    class Meta:
        model = Creator
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'avatar',
        'description', 'console', 'rank', 'hours_played', 'pictures']

class UserUpdateForm(d_forms.ModelForm):
    model = Creator, Consumer
    fields = ['username', 'email', 'avatar']

class ProfileUpdateForm(d_forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['description', 'console', 'rank', 'hours_played', 'pictures']