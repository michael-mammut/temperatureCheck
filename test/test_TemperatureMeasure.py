#!/usr/bin/env python3

from datetime import datetime
from unittest import TestCase, mock

from Entities.TemperatureMeasure import TemperatureMeasure
from Entities.TemperatureMeasure import MeasureResult


class test_TemperatureMeasure(TestCase):
    def test_name(self):
        t = TemperatureMeasure(measurement_name="TestMedium", sensor_id="-2", sensor_label="Water", reference_sensor_id="-3",
                               reference_label="Ambient")
        self.assertEqual("TestMedium", t.name)
        self.assertEqual("-2", t.sensor_id)

    def test_fail_name(self):
        t = TemperatureMeasure(measurement_name="TestMedium", sensor_id="-2B", sensor_label="Water-B", reference_sensor_id="-3B",
                               reference_label="AmbientB")
        self.assertNotEqual("FAIL", t.name)
        self.assertEqual("-2B", t.sensor_id)


    def test_MeasureResult_with_params(self):
        mock_created_at = datetime.now()

        with mock.patch.object(MeasureResult, 'get_now', return_value=mock_created_at):
            r = MeasureResult(21, 10)
            self.assertDictEqual({"value": 21, "ambient": 10, "created_at": mock_created_at}, r.__dict__)
