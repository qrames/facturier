from django.template.defaultfilters import slugify
from django.db.models import SlugField
from django.contrib.gis.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from django_extensions.db.fields import AutoSlugField


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, default="")
    last_name = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from=['first_name', 'last_name'])
    business = models.CharField(max_length=150, null=True)
    siren = models.IntegerField()
    logo = models.ImageField(upload_to="user", null=True)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=250, null=True, blank=True)
    phone_number = PhoneNumberField()
    fax_number = PhoneNumberField(blank=True)

    def __unicode__(self):
        return self.slug


class Product(models.Model):
    code = models.SlugField(max_length=8)
    name = models.CharField(max_length=150)
    description = models.TextField()
    short_desc = models.CharField(max_length=150)
    pics = models.ImageField(upload_to="media/product")
    price = models.FloatField(max_length=10)

    def __unicode__(self):
        return self.name


class QuotationLine(models.Model):
    quotation = models.ForeignKey('Quotation', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class BillLine(models.Model):
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


STATUS_CHOICES = (
    ('A relancer', 'A relancer'),
    ('En cours', 'En cours'),
    ('A convertir', 'A convertir'),
)


class Quotation(models.Model):
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(
        "Customer", verbose_name=("client"), on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, choices=STATUS_CHOICES, default='A relancer')




class Bill(models.Model):
    date = models.DateTimeField(auto_now=True)
    quotation = models.ForeignKey(
        "Quotation", verbose_name=("devis"), on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, default='En attente de reglement')
