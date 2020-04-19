#!/usr/bin/env python3
from pushbullet import PushBullet

from Entities.TemperatureMeasure import MeasureResult
from Settings.constants import NOTIFICATIONTYPE
from Settings.tokens import PUSHBULLETTOKEN
from Settings.temperature_settings import TEMPERATURE_LIMITS


class NotificationServiceFactory:
    def __init__(self, type, measure_result, title='Notification title'):
        if type is None or not isinstance(measure_result,
                                          MeasureResult) or measure_result.value is None or measure_result.ambient is None:
            raise TypeError('None is not allowed')
        self._type = type
        self._measureResult = measure_result
        self._title = self._get_notification_title()
        self._message = "Wassertemp. liegt bei: " + str(self._measureResult.value) + "°C. Raumtemperatur bei " + str(
            self._measureResult.ambient) + "°C"

    def get_notification_service(self):
        if self._type is NOTIFICATIONTYPE.get('MOBILE'):
            return MobileNotificationService(self._measureResult, self._title)

        raise TypeError('Notificationtype does not exists')

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
            return  "ACHTUNG! ZU WARME TEMPERATUR"
        else:
            return "INFORMATION"

    def notify(self):
        pass

class MobileNotificationService(NotificationServiceFactory):

    def __init__(self, measure_result, title='Pushbullet Title'):
        super().__init__(NOTIFICATIONTYPE.get('MOBILE'), measure_result, title)

    def notify(self):
        pb = PushBullet(PUSHBULLETTOKEN)
        pb.push_note(self._title, self._message)
