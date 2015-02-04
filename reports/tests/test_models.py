from django.test import TestCase

from reports.models import Report

class ReportModelTest(TestCase):
	def test_model_fields(self):
        """
        test that model contains certain fields
        """
        fields = {field.name: field for field in Report._meta.fields}

        self.assertTrue(fields.has_key('title'))
        self.assertTrue(fields.has_key('content'))
        self.assertTrue(fields.has_key('author'))
        self.assertTrue(fields.has_key('applicant'))
        self.assertTrue(fields.has_key('updated'))
        self.assertTrue(fields.has_key('created_at'))
        self.assertTrue(fields.has_key('is_public'))

	def test_string_representation(self):
		report = Report(title="My Title")
		self.assertEqual(str(report), report.title)