from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'birthday',)


class CustomUserChangeForm(UserChangeForm):
    birthday = forms.DateField(
        widget = forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    password= None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'username', 'birthday',)