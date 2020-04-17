from unittest import TestCase

from Repository.NotificationRepository import PushBulletNotification


class TestPushBulletNotification(TestCase):

    def test_init(self):
        with self.assertRaisesRegex(TypeError, 'None is not allowed') as cm:
            nr = PushBulletNotification(None, None)

    def test_get_message(self):
        nr = PushBulletNotification(10, 30)
        self.assertEqual("Wassertemp. liegt bei: 10°C. Raumtemperatur bei 30°C", nr.get_message())

