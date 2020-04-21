from unittest import TestCase

from Entities.TemperatureMeasure import MeasureResult
from Services.NotificationServiceFactory import MobileNotificationService, NotificationServiceFactory
from Settings.constants import NOTIFICATIONTYPE
from Settings.temperature_settings import TEMPERATURE_LIMITS


class TestNotificationService(TestCase):

    def setUp(self):
        self.__AMBIENT = 30
        self.__measureResult = MeasureResult(10, self.__AMBIENT)
        self.__typeMobile = NOTIFICATIONTYPE.get('MOBILE')

    def test_init(self):
        with self.assertRaisesRegex(TypeError, 'None is not allowed') as cm:
            nr = MobileNotificationService(None, None)

    def test_get_message(self):
        nr = MobileNotificationService(self.__measureResult, 'Test Title')
        self.assertEqual("Wassertemp. liegt bei: 10°C. Raumtemperatur bei 30°C", nr.get_message())

    def test_get_notification_by_type(self):

        self.assertIsInstance(NotificationServiceFactory(self.__typeMobile, self.__measureResult).get_notification_service(),
                              MobileNotificationService)

    def test_get_notification_by_type_fail(self):
        type = -1
        with self.assertRaisesRegex(TypeError, 'Notificationtype does not exists'):
            NotificationServiceFactory(type, self.__measureResult).get_notification_service()

    def test_title_by_temperature_information(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('SETPOINT'), self.__AMBIENT)
        n = NotificationServiceFactory(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('INFORMATION', n.get_title())

    def test_title_by_temperature_warning_cold(self):
        rm = MeasureResult(10, self.__AMBIENT)
        n = NotificationServiceFactory(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! GERINGE TEMPERATUR', n.get_title())

    def test_title_by_temperature_warning_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('WARNING'), self.__AMBIENT)
        n = NotificationServiceFactory(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! WARME TEMPERATUR', n.get_title())

    def test_title_by_temperature_alert_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('ALERT'), self.__AMBIENT)
        n = NotificationServiceFactory(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! ZU WARME TEMPERATUR', n.get_title())