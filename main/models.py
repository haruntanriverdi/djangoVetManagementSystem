from django.db import models
from django.contrib.auth import get_user_model


class Pets(models.Model):

    name = models.CharField(max_length=200, verbose_name='Pet Name')
    type = models.CharField(max_length=200, verbose_name='Pet Type')
    breed = models.CharField(max_length=200,  verbose_name='Breed')
    age = models.PositiveIntegerField(verbose_name='Pet Age', null=True)
    description = models.TextField(blank=True, verbose_name='Description')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = ' Pets'


class Owners(models.Model):
    pet = models.ManyToManyField(Pets, verbose_name='Pets')
    name = models.CharField(max_length=500, verbose_name='İsim')
    email = models.EmailField( verbose_name='İsim')
    address = models.CharField(max_length=500, verbose_name='Address')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    description = models.TextField(blank=True, max_length=225, verbose_name='Description')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

