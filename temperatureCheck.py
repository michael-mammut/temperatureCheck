#!/usr/bin/env python3

from Repository.CsvDataRepository import CsvDataRepository
from Services.NotificationService import NotificationService, NotificationServiceFactory
from Settings.constants import *
from Module.Temperature.temperature_settings import WATER_SENSOR_ID, AMBIETEN_SENSOR_ID
from Settings.datastore import TEMPERATURE_DATA_FILE
from Module.Temperature.TemperatureSensor import TemperatureSensor
import sys

temperatureSensor = TemperatureSensor('Aquarium', WATER_SENSOR_ID, 'Wassertemperatur', AMBIETEN_SENSOR_ID)
measurer_result = temperatureSensor.get_temperature_in_celsius()

data_repo = CsvDataRepository(TEMPERATURE_DATA_FILE, ['value', 'ambient', 'created_at'])
data_repo.add(measurer_result)

if(len(sys.argv)>1):
    notificationType = sys.argv[1].upper()
else:
    notificationType = TELEGRAM

notification_service = NotificationServiceFactory().getNotificationService(notificationType, measurer_result)
notification_service.notify()
