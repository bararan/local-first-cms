from django.db import models


class OrganizationDescription(models.Model):
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
