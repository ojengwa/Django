from django.test import TestCase
from application.models import Listing
# Create your tests here.

class ListingModelTest(TestCase):

    def test_model_fields(self):
        
        """
        test that model contains certain fields
        """
        fields = {field.name: field for field in Listing._meta.fields}

        self.assertTrue(fields.has_key('listing'))
        self.assertTrue(fields.has_key('description'))
        self.assertTrue(fields.has_key('end_date'))
        self.assertTrue(fields.has_key('updated'))
        self.assertTrue(fields.has_key('created_at'))

    def test_string_representation(self):
    	listing = Listing(listing="My Listing")
    	self.assertEqual(str(listing), listing.listing)