'''
    End to end tests for the values part of the platform

'''
from unittest import skip
from django.test import TestCase
from selenium import webdriver

# Keyboard keys
from selenium.webdriver.common.keys import Keys


class FrontEndTest(TestCase):
    """docstring for FrontEndTest"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        pass

    def tearDown(self):
        self.browser.quit()
        pass


    def test_homepage(self):
        self.browser.get('http://google.com')
        self.q = self.browser.find_element_by_name('q')
        self.q.send_keys('Ojengwa')
        self.q.send_keys(Keys.RETURN)

        assert 'Ojengwa Bernard' in self.browser.page_source
        pass

    @skip('Will implement test_registration later')
    def test_registration(self):
        pass

    @skip('Will do later')
    def test_about(self):
        pass