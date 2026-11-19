# from unittest.mock import patch

# from django.test import SimpleTestCase

# from .models import User


# class UserManagerTests(SimpleTestCase):
#     def test_get_by_natural_key_uses_email_field(self):
#         with patch.object(User.objects, 'get') as get:
#             User.objects.get_by_natural_key('person@example.com')

#         get.assert_called_once_with(email='person@example.com')
