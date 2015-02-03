from django.test import TestCase

# Create your tests here.
from users.models import Applicant

class AppplicantModelTests(TestCase):

    def test_model_fields(self):
        """
        test that model contains certain fields
        """
        fields = {field.name: field for field in Applicant._meta.fields}

       	self.assertTrue(fields.has_key('user'))
        self.assertTrue(fields.has_key('first_name'))
        self.assertTrue(fields.has_key('last_name'))
        self.assertTrue(fields.has_key('phone_number'))
        self.assertTrue(fields.has_key('address'))
        self.assertTrue(fields.has_key('cv'))
        self.assertTrue(fields.has_key('cover_letter'))
        self.assertTrue(fields.has_key('application_date'))
        self.assertTrue(fields.has_key('is_valid'))
        self.assertTrue(fields.has_key('is_active'))

