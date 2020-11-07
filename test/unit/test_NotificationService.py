from unittest import TestCase

from Module.Temperature.MeasureResult import MeasureResult
from Services.NotificationService import MobileNotificationService, NotificationService
from Settings.constants import NOTIFICATIONTYPE
from Module.Temperature.temperature_settings import TEMPERATURE_LIMITS


class TestNotificationService(TestCase):

    def setUp(self):
        self.__AMBIENT = 30
        self.__measureResult = MeasureResult(10, self.__AMBIENT)
        self.__typeMobile = NOTIFICATIONTYPE.get('TELEGRAM')

    def test_get_message(self):
        nr = MobileNotificationService(self.__measureResult)
        self.assertEqual("Wassertemp. liegt bei: 10°C. Raumtemperatur bei 30°C", nr.get_message())

    def test_get_notification_by_type(self):
        self.assertIsInstance(NotificationService(self.__typeMobile, self.__measureResult).get_notification_service(),
                              NotificationService)

    def test_get_notification_by_type_fail(self):
        dummy_type = -1
        with self.assertRaisesRegex(TypeError, 'Notificationtype does not exists'):
            NotificationService(dummy_type, self.__measureResult).get_notification_service()

    def test_title_by_temperature_information(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('SETPOINT'), self.__AMBIENT)
        n = NotificationService(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('INFORMATION', n.get_title())

    def test_title_by_temperature_warning_cold(self):
        rm = MeasureResult(10, self.__AMBIENT)
        n = NotificationService(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! GERINGE TEMPERATUR', n.get_title())

    def test_title_by_temperature_warning_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('WARNING'), self.__AMBIENT)
        n = NotificationService(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! WARME TEMPERATUR', n.get_title())

    def test_title_by_temperature_alert_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('ALERT'), self.__AMBIENT)
        n = NotificationService(self.__typeMobile, rm).get_notification_service()
        self.assertEqual('ACHTUNG! ZU WARME TEMPERATUR', n.get_title())

    # MANUAL TESTING ONLY
    # def test_runNotification(self):
    #     rm = MeasureResult(TEMPERATURE_LIMITS.get('ALERT'), -100)
    #     n = NotificationService(self.__typeMobile, rm).get_notification_service()
    #     n.notify()
