from django.test import TestCase
from . models import OrganizationDescription


class DescriptionTestCase(TestCase):
    def setUp(self):
        OrganizationDescription.objects.create(title="Local First",
                                               description="This is a test",
                                               link="www.google.com")

    def test_description_is_created(self):
        local_first = OrganizationDescription.objects.get(title="Local First")
        self.assertEqual(local_first.title, "Local First")
        self.assertEqual(local_first.description, "This is a test")
        self.assertEqual(local_first.link, "www.google.com")


# class AddressTestCase(TestCase):
#     def setUp(self):
#       TODO add the rest of the model tests