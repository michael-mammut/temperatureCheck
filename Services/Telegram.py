import requests

from Services.NotificationService import NotificationService
import urllib.parse
import http.client
from Settings.tokens import BOT_TOKEN, GROUP_ID


class Telegram(NotificationService):

    def __init__(self,measure_result):
        super().__init__(measure_result)

    def notify(self):
        messageCode = urllib.parse.quote_plus(self.get_message())
        url = "/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + GROUP_ID + "&text=" + messageCode

        conn = http.client.HTTPSConnection('api.telegram.org')
        conn.request('GET', url)
        conn.getresponse()

    # return the last message of the bot, not a group
    def readDataFromBot(self):
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
        response = requests.post(url).json()
        return response['result'][len(response['result'])-1]['message']['text']
        # abfangen aller möglichen nachrichtentypen durch den User
        # nur texte zulassen
        # text
        # - Foto
        # - Video
        # - Temperatur
        # - Aktor XY ein
        # - Aktor XY aus
        # - SET AKTOR <XY> ON AT <time>
        # - SET AKTOR <xy> OFF AT <time>
        # - ALL STATUS

    def sendImage(self, filepath: str, caption: str):
        with open(filepath, 'rb') as f:
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto?'
            data = {
               'chat_id': f'-{GROUP_ID}',
               'caption': caption
                     }
            files = {
                'photo': f.read()
            }
            response = requests.post(url=url, data=data, files=files).json()
            f.close()
            return response

