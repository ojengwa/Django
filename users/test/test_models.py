from django.test import TestCase

from users.models import User
from users.models import UserManager


class UserModelTests(TestCase):

    def test_model_fields(self):
        """
        test that model contains certain fields
        """
        fields = {field.name: field for field in User._meta.fields}

        self.assertTrue(fields.has_key('email'))
        self.assertTrue(fields.has_key('first_name'))
        self.assertTrue(fields.has_key('last_name'))
        self.assertTrue(fields.has_key('phone_number'))
        self.assertTrue(fields.has_key('address'))
        self.assertTrue(fields.has_key('is_admin'))

    def test_get_short_name(self):
        """
        get_short_name() should return User first_name
        """
        user = User(first_name = 'jason', last_name = 'swett', email = 'jason@gmail.com')

        self.assertEqual(user.get_short_name(), 'jason')

    def test_get_full_name(self):
        """
        get_short_name() should return User first_name
        """
        user = User(first_name = 'jason', last_name = 'swett', email = 'jason@gmail.com')

        self.assertEqual(user.get_full_name(), 'jason swett')


class UserManagerTest(TestCase):

    def test_create_user(self):
        """
        create_user() should create and return user
        """

        user = UserManager()
        user.create_user(email = "jason@gmail.com", password = "jasonswett", username = "jasonswett")

        self.assertEqual(user.email, "jason@gmail.com")
