from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Kullanıcı adı",
                "class": "form-control",
                "id": "login-username",
                "name": "login-username",

            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Şifre",
                "class": "form-control",
                "id": "login-password",
                "name": "login-password",
            }
        ))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))

    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   label='Authorization',
                                   widget=forms.Select(attrs={"class": "form-select",}))

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Password Again',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "password again",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'group')