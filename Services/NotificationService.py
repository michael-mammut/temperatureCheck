#!/usr/bin/env python3
from pushbullet import PushBullet

from Module.Temperature.MeasureResult import MeasureResult
from Settings.constants import *
from Module.Temperature.temperature_settings import TEMPERATURE_LIMITS


class NotificationService:

    def __init__(self, measure_result):
        self.setNotificationData(measure_result)

    def setNotificationData(self, measure_result):
        self._measureResult = measure_result
        self._title = self._get_notification_title()
        self._message = "Wassertemp. liegt bei: " + str(self._measureResult.value) + "°C. Raumtemperatur bei " + str(
            self._measureResult.ambient) + "°C"
        return self

    # Implementaion to send a message
    def notify(self):
        pass

    def get_message(self):
        return self._message

    def get_title(self):
        return self._title

    def _get_notification_title(self):
        if self._measureResult.value < TEMPERATURE_LIMITS["SETPOINT"]:
            return "ACHTUNG! GERINGE TEMPERATUR"
        elif TEMPERATURE_LIMITS["WARNING"] <= self._measureResult.value < TEMPERATURE_LIMITS["ALERT"]:
            return "ACHTUNG! WARME TEMPERATUR"
        elif self._measureResult.value >= TEMPERATURE_LIMITS["ALERT"]:
            return "ACHTUNG! ZU WARME TEMPERATUR"
        else:
            return "INFORMATION"


class NotificationServiceFactory():
    def getNotificationService(self, type, measure_result):
        if type is PUSHBULLET:
            from Services.Pushbullet import Pushbullet
            return Pushbullet(measure_result)

        if type is TELEGRAM:
            from Services.Telegram import Telegram
            return Telegram(measure_result)

        raise TypeError('Notificationtype does not exists')