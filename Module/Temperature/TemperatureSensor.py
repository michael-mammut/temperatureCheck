#!/usr/bin/env python3
from Module.Temperature.MeasureResult import MeasureResult


class TemperatureSensor:

    def __init__(self, measurement_name, sensor_id, sensor_label, reference_sensor_id, reference_label='Ambient'):
        self.__name = measurement_name
        self.__sensor_id = sensor_id
        self.__sensor_label = sensor_label
        self.__reference_sensor_id = reference_sensor_id
        self.__reference_sensor_label = reference_label

    @property
    def name(self):
        return self.__name

    @property
    def sensor_id(self):
        return self.__sensor_id

    @property
    def reference_sensor_id(self):
        return self.__reference_sensor_id

    def get_temperature_in_celsius(self) -> MeasureResult:
        water = self._get_temperature_in_celsius_by_sensor(self.sensor_id)
        reference_sensor = self._get_temperature_in_celsius_by_sensor(self.reference_sensor_id)
        return MeasureResult(water, reference_sensor)

    def _get_temperature_in_celsius_by_sensor(self, sensor_id):
        from w1thermsensor import W1ThermSensor

        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensor_id)
        return sensor.get_temperature(W1ThermSensor.DEGREES_C)
