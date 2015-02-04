'''
    End to end tests for the values part of the platform

'''
from unittest import skip
from django.test import TestCase
from selenium import webdriver

# Keyboard keys and UI elements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui


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
        self.browser.get('http://localhost:8000')
        # self.q = self.browser.find_element_by_name('q')
        # self.q.send_keys('Ojengwa')
        # self.q.send_keys(Keys.RETURN)

        assert 'Django' in self.browser.title


    @skip('Will implement test_registration later')
    def test_registration(self):
        pass

    @skip('Will do later')
    def test_about(self):
        pass

@skip
class BackendTest(TestCase):
    """docstring for BackendTest"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        pass

