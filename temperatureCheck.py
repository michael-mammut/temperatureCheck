#!/usr/bin/env python3
from Entities.TemperatureMeasure import TemperatureMeasure
from Services.NotificationServiceFactory import NotificationServiceFactory
from Services.TemperatureService import TemperatureService
from Settings.constants import NOTIFICATIONTYPE
from Settings.temperature_settings import WATER_SENSOR_ID, AMBIETEN_SENSOR_ID

temperatureService = TemperatureService(TemperatureMeasure(measurement_name='Aquarium', sensor_id=WATER_SENSOR_ID,
                                                           sensor_label='Wassertemperatur',
                                                           reference_sensor_id=AMBIETEN_SENSOR_ID))
measurer_result = temperatureService.get_temperature_in_celsius()

notification_service = NotificationServiceFactory(NOTIFICATIONTYPE.get('MOBILE'), measurer_result)
mobile = notification_service.get_notification_service()
mobile.notify()
