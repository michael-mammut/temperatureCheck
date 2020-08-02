#!/usr/bin/env python3

from unittest import TestCase, mock

from Module.Temperature.MeasureResult import MeasureResult
from Module.Temperature.TemperatureSensor import TemperatureSensor


class TestTemperature(TestCase):


    def test_get_temperature_in_celsius(self):
        with mock.patch.object(TemperatureSensor, '_get_temperature_in_celsius_by_sensor',
                               return_value=-273):
            temperatureMeasure = TemperatureSensor(measurement_name="TestMedium", sensor_id="-2B", sensor_label="Water-B",
                                                   reference_sensor_id="-3B", reference_label="AmbientB")

            result = temperatureMeasure.get_temperature_in_celsius()
            self.assertIsInstance(type(result), type(MeasureResult))
