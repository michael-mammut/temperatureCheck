#!/usr/bin/env python3

from Entities.TemperatureMeasure import MeasureResult, TemperatureMeasure


class TemperatureService:

    def __init__(self, temperature_measure):

        if isinstance(temperature_measure, TemperatureMeasure):
            self._temperature_measure = temperature_measure
        else:
            raise TypeError('Wrong type is given')


    def get_temperature_in_celsius(self) -> MeasureResult:
        water = self._get_temperature_in_celsius_by_sensor(self._temperature_measure.sensor_id)
        reference_sensor = self._get_temperature_in_celsius_by_sensor(self._temperature_measure.reference_sensor_id)
        return MeasureResult(water, reference_sensor)

    def _get_temperature_in_celsius_by_sensor(self, sensor_id):
        from w1thermsensor import W1ThermSensor

        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensor_id)
        return sensor.get_temperature(W1ThermSensor.DEGREES_C)
