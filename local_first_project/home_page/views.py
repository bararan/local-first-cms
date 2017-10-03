from django.shortcuts import render
from .models import OrganizationDescription


def index(request):
    description = OrganizationDescription.
