#!/usr/bin/env python3

from unittest import TestCase, mock

from Entities.TemperatureMeasure import MeasureResult, TemperatureMeasure
from Services.TemperatureService import TemperatureService


class TestTemperatureService(TestCase):

    def test_init(self):
       with self.assertRaisesRegex(TypeError, 'Wrong type is given'):
           TemperatureService(1)


    def test_get_temperature_in_celsius(self):
        with mock.patch.object(TemperatureService, '_get_temperature_in_celsius_by_sensor',
                               return_value=-273) as mock_masure_result:
            temperatureMeasure = TemperatureMeasure(measurement_name="TestMedium", sensor_id="-2B", sensor_label="Water-B",
                                                    reference_sensor_id="-3B", reference_label="AmbientB")

            r = TemperatureService(temperatureMeasure)
            result = r.get_temperature_in_celsius()
            self.assertIsInstance(type(result), type(MeasureResult))