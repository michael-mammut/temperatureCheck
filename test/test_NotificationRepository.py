from unittest import TestCase

from Entities.TemperatureMeasure import MeasureResult
from Services.NotificationServiceFactory import MobileNotificationService, NotificationServiceFactory
from Settings.Constants import NOTIFICATIONTYPE


class TestPushBulletNotification(TestCase):

    def setUp(self):
        self.__measureResult = MeasureResult(10, 30)

    def test_init(self):
        with self.assertRaisesRegex(TypeError, 'None is not allowed') as cm:
            nr = MobileNotificationService(None, None)

    def test_get_message(self):
        nr = MobileNotificationService(self.__measureResult, 'Test Title')
        self.assertEqual("Test Title", nr.get_title())
        self.assertEqual("Wassertemp. liegt bei: 10°C. Raumtemperatur bei 30°C", nr.get_message())

    def test_get_notification_by_type(self):
        type = NOTIFICATIONTYPE.get('MOBILE')
        self.assertIsInstance(NotificationServiceFactory(type, self.__measureResult).get_notification_service(),
                              MobileNotificationService)

    def test_get_notification_by_type_fail(self):
        type = -1
        with self.assertRaisesRegex(TypeError, 'Notificationtype does not exists'):
            NotificationServiceFactory(type, self.__measureResult).get_notification_service()
