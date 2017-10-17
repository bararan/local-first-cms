from django.db import models
from filer.fields.image import FilerImageField


class OrganizationDescription(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)


class BannerImage(models.Model):
    img = FilerImageField(null=True, blank=True)


class BusinessAddress(models.Model):
    address = models.TextField()


class Contact(models.Model):
    email = models.EmailField()
    phone = models.TextField()


class Card(models.Model):
    img = FilerImageField(null=True, blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)


class Footer(models.Model):
    text = models.CharField(max_length=128)
