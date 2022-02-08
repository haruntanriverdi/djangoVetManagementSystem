from django import forms
from .models import Pets, Owners
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class PetForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pet Name",
                "class": "form-control"
            }
        ))

    type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pet Type",
                "class": "form-control"
            }
        ))
    breed = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pet Breed",
                "class": "form-control"
            }
        ))

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Pet Age",
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Pets
        fields = ('name', 'type', 'breed', 'age', 'description')


class OwnersForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ))

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        ))

    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "form-control"
            }
        ))

    pet = forms.ModelMultipleChoiceField(
        queryset=Pets.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select", "size":5})
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Owners
        fields = ('name', 'email', 'address', 'phone', 'pet','description')