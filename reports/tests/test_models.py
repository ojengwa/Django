from django.test import TestCase

from reports.models import Report

class ReportModelTest(TestCase):

	def test_string_representation(self):
		report = Report(report_title="My Title")
		self.assertEqual(str(report), report.title)

	def test_string_representation(self):
		report = Report(report_title="My Title")
		self.assertEqual(str(report), report.content)