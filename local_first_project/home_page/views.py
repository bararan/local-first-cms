from django.shortcuts import render
from .models import OrganizationDescription, BannerImage, BusinessAddress, \
    Contact, Card, Footer


def index(request):
    description = OrganizationDescription.objects.all()
    banner = BannerImage.objects.all()
    address = BusinessAddress.objects.all()
    contact = Contact.objects.all()
    cards = Card.objects.all()
    footer = Footer.objects.all()
    context_dict = {'description': description,
                    'banner': banner,
                    'address': address,
                    'contact': contact,
                    'cards': cards,
                    'footer': footer,
                    }
    return render(request, 'home_page/index.html', context_dict)
# TODO add index to templates in home_page