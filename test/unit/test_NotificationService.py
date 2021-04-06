from unittest import TestCase

from Module.Temperature.MeasureResult import MeasureResult
from Module.Temperature.temperature_settings import TEMPERATURE_LIMITS
from Services.NotificationService import NotificationService, NotificationServiceFactory
from Services.Telegram import Telegram
from Settings.constants import TELEGRAM


class TestNotificationService(TestCase):

    def setUp(self):
        self.__AMBIENT = 30
        self.__measureResult = MeasureResult(10, self.__AMBIENT)
        self.__typeMobile = TELEGRAM

    def test_get_message(self):
        nr = Telegram(self.__measureResult)
        self.assertEqual("Wassertemp. liegt bei: 10°C. Raumtemperatur bei 30°C", nr.get_message())

    def test_get_notification_by_type(self):
        self.assertIsInstance(NotificationServiceFactory().getNotificationService(self.__typeMobile, self.__measureResult),
                              NotificationService)

    def test_get_notification_by_type_fail(self):
        dummy_type = -1
        with self.assertRaisesRegex(TypeError, 'Notificationtype does not exists'):
            NotificationServiceFactory().getNotificationService('dummy', self.__measureResult)

    def test_title_by_temperature_information(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('SETPOINT'), self.__AMBIENT)
        notificationService = NotificationServiceFactory().getNotificationService(self.__typeMobile, rm)
        self.assertEqual('INFORMATION', notificationService.get_title())

    def test_title_by_temperature_warning_cold(self):
        rm = MeasureResult(10, self.__AMBIENT)
        n = NotificationServiceFactory().getNotificationService(self.__typeMobile, rm)
        self.assertEqual('ACHTUNG! GERINGE TEMPERATUR', n.get_title())

    def test_title_by_temperature_warning_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('WARNING'), self.__AMBIENT)
        n = NotificationServiceFactory().getNotificationService(self.__typeMobile, rm)
        self.assertEqual('ACHTUNG! WARME TEMPERATUR', n.get_title())

    def test_title_by_temperature_alert_warm(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('ALERT'), self.__AMBIENT)
        n = NotificationServiceFactory().getNotificationService(self.__typeMobile, rm)
        self.assertEqual('ACHTUNG! ZU WARME TEMPERATUR', n.get_title())

