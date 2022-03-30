from django.test import TestCase
from django.contrib.auth import get_user_model


class ProfileTestCase(TestCase):

    def test_profile_image(self):
        user1 = get_user_model().objects.create(
            username='test1',
            password='pepepe123'
        )
        self.assertEqual(bool(user1.profile), True)
        self.assertEqual(user1.profile.image.name, 'default.jpg')
