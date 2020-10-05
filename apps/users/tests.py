from django.test import TestCase
from .models import CustomUser

class UsersManagersTests(TestCase):

    def test_create_user(self):
        test_user = CustomUser.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(test_user.email, 'normal@user.com')
        self.assertTrue(test_user.is_active)
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(test_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CustomUser.objects.create_user()
        with self.assertRaises(TypeError):
            # pylint: disable=no-value-for-parameter
            CustomUser.objects.create_user(email='')
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
