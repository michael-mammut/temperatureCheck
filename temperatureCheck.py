#!/usr/bin/env python3

import Entities.TemperatureSensor
from Repository.CsvDataRepository import CsvDataRepository
from Services.NotificationServiceFactory import NotificationServiceFactory
from Settings.constants import NOTIFICATIONTYPE
from Settings.temperature_settings import WATER_SENSOR_ID, AMBIETEN_SENSOR_ID
from Settings.datastore import TEMPERATURE_DATA_FILE
from Entities.TemperatureSensor import TemperatureSensor

temperatureSensor = TemperatureSensor('Aquarium', WATER_SENSOR_ID, 'Wassertemperatur', AMBIETEN_SENSOR_ID)
measurer_result = temperatureSensor.get_temperature_in_celsius()

data_repo = CsvDataRepository(TEMPERATURE_DATA_FILE)
data_repo.add(measurer_result)

notification_service = NotificationServiceFactory(NOTIFICATIONTYPE.get('MOBILE'), measurer_result)
mobile = notification_service.get_notification_service()
mobile.notify()
