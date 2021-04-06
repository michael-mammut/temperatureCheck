import unittest

from Module.Temperature.MeasureResult import MeasureResult
from Module.Temperature.temperature_settings import TEMPERATURE_LIMITS
from Services.NotificationService import NotificationServiceFactory
from Settings.enviroment import ENVIROMENT
from Settings.constants import PRODUCTION, TELEGRAM
from Services.Telegram import Telegram


# About all the test in this test class
# to check, is the bot available and get the last message of long polling
# there is no assertation because it to verify visual with the eyes

class MyTestCase(unittest.TestCase):

    @unittest.skipIf(ENVIROMENT == PRODUCTION, 'We do not run this test in production enviroment')
    def test_readDataFromBot(self):
        # Send "TestMessage" by phone or web.telegram to your bot
        self.assertEqual('TestMessage', Telegram.readDataFromBot(self))

    @unittest.skipIf(ENVIROMENT == PRODUCTION, 'We do not run this test in production enviroment')
    def test_sendImage(self):
        result = Telegram.sendImage(self,'test-image.jpg', 'Sendet test image')
        self.assertTrue(result['ok'])

    @unittest.skipIf(ENVIROMENT == PRODUCTION, 'We do not run this test in production enviroment')
    def test_sendMessage(self):
        result = Telegram.notify(self)
        self.assertTrue(result['ok'])

    # MANUAL TESTING ONLY
    @unittest.skipIf(ENVIROMENT == PRODUCTION, 'We do not run this test in production enviroment')
    def test_runNotification(self):
        rm = MeasureResult(TEMPERATURE_LIMITS.get('ALERT'), -100)
        n = NotificationServiceFactory().getNotificationService(TELEGRAM, rm)
        n.notify()

if __name__ == '__main__':
    unittest.main()
