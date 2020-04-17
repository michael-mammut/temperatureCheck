#!/usr/bin/env python3

from unittest import TestCase, mock

from Entities.TemperatureMeasure import MeasureResult, TemperatureMeasure
from Repository.TemperatureRepository import TemperatureRepository


class TestTemperatureRepository(TestCase):

    def test_init(self):
       with self.assertRaisesRegex(TypeError, 'Wrong type is given'):
           TemperatureRepository(1)


    def test_get_temperature_in_celsius(self):
        with mock.patch.object(TemperatureRepository, '_get_temperature_in_celsius_by_sensor',
                               return_value=-273) as mock_masure_result:
            temperatureMeasure = TemperatureMeasure(name="TestMedium", sensor_id="-2B", sensor_label="Water-B",
                                   reference_sensor_id="-3B", reference_label="AmbientB")

            r = TemperatureRepository(temperatureMeasure)
            result = r.get_temperature_in_celsius()
            self.assertIsInstance(type(result), type(MeasureResult))
