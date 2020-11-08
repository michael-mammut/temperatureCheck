from pushbullet import PushBullet

from Services.NotificationService import NotificationService
from Settings.tokens import PUSHBULLETTOKEN


class Pushbullet(NotificationService):

    def __init__(self, measure_result):
        super().__init__(measure_result)

    def notify(self):
        pb = PushBullet(PUSHBULLETTOKEN)
        pb.push_note(self._title, self._message)