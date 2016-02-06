from django.test import TestCase
from selenium import webdriver

# Create your tests here.

class SimpleTest(TestCase):
    """docstring for SimpleTest"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_addition(self):
        self.assertEqual(1+2, 3)

    def test_web(self):
        self.browser.get('http://localhost:8000')

        assert 'Django' in self.browser.title

    def tearDown(self):
        self.browser.quit()

        return 0