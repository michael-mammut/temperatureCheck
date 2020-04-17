#!/usr/bin/env python3

from Entities.TemperatureMeasure import MeasureResult, TemperatureMeasure


class TemperatureRepository:

    def __init__(self, temperatureMeasure):

        if isinstance(temperatureMeasure, TemperatureMeasure):
            self._temperatureMeasure = temperatureMeasure
        else:
            raise TypeError('Wrong type is given')


    def get_temperature_in_celsius(self):
        water = self._get_temperature_in_celsius_by_sensor(self._temperatureMeasure.sensor_id)
        reference_sensor = self._get_temperature_in_celsius_by_sensor(self._temperatureMeasure.reference_sensor_id)
        return MeasureResult(water, reference_sensor)

    def _get_temperature_in_celsius_by_sensor(self, sensorId):
        from w1thermsensor import W1ThermSensor

        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensorId)
        return sensor.get_temperature(W1ThermSensor.DEGREES_C)
