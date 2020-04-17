#!/usr/bin/env python3
from pushbullet import PushBullet
from Settings.settings import PUSHBULLETTOKEN


class NotificationRepository:
    def __init__(self, value, ambient, title = 'no title'):

        if value is None or ambient is None:
            raise TypeError('None is not allowed')

        self._value = value
        self._ambient = ambient
        self._title = title
        self._message = "Wassertemp. liegt bei: " + str(self._value) + "°C. Raumtemperatur bei " + str(
            self._ambient) + "°C"

    def get_message(self):
        return self._message

    def notify(self):
        pass


class PushBulletNotification(NotificationRepository):

    def __init__(self, value, ambient):
        super().__init__(value, ambient)

    def notify(self):
        pb = PushBullet(PUSHBULLETTOKEN)
        pb.push_note(self._title, self._message)