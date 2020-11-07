from Services.NotificationService import NotificationService
import urllib.parse
import http.client
from Settings.tokens import BOT_TOKEN, GROUP_ID
from Settings.constants import NOTIFICATIONTYPE


class Telegram(NotificationService):

    def __init__(self, measure_result):
        super().__init__(NOTIFICATIONTYPE.get('MOBILE'), measure_result)


    def notify(self):
        # @radio_watch_bot
        messageCode = urllib.parse.quote_plus(self.get_message())
        url = "/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + GROUP_ID + "&text=" + messageCode

        conn = http.client.HTTPSConnection('api.telegram.org')
        conn.request('GET', url)
        conn.getresponse()


