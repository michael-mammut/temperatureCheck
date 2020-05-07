#!/usr/bin/env python3

import Entities.TemperatureMeasure
from Repository.DataRepository import DataRepository
from Services.NotificationServiceFactory import NotificationServiceFactory
from Services.TemperatureService import TemperatureService
from Settings.constants import NOTIFICATIONTYPE
from Settings.temperature_settings import WATER_SENSOR_ID, AMBIETEN_SENSOR_ID
from Settings.datastore import TEMPERATURE_DATA_FILE

temperatureService = TemperatureService(Entities.TemperatureMeasure.TemperatureMeasure(measurement_name='Aquarium', sensor_id=WATER_SENSOR_ID,
                                                                                       sensor_label='Wassertemperatur',                                                                              reference_sensor_id=AMBIETEN_SENSOR_ID))
measurer_result = temperatureService.get_temperature_in_celsius()

data_repo = DataRepository(TEMPERATURE_DATA_FILE)
data_repo.add(measurer_result)

notification_service = NotificationServiceFactory(NOTIFICATIONTYPE.get('MOBILE'), measurer_result)
mobile = notification_service.get_notification_service()
mobile.notify()
