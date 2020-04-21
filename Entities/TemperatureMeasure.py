#!/usr/bin/env python3
import time
from datetime import datetime


class TemperatureMeasure:

    def __init__(self, measurement_name, sensor_id, sensor_label, reference_sensor_id, reference_label = 'Ambient'):
        self.__name = measurement_name
        self.__sensor_id = sensor_id
        self.__sensor_label = sensor_label
        self.__reference_sensor_id = reference_sensor_id
        self.__reference_sensor_label = reference_label
        self.__created_at = time.time()
        self.tricks = []

    @property
    def name(self):
        return self.__name

    @property
    def sensor_id(self):
        return self.__sensor_id

    @property
    def value(self):
        return self.__value

    @property
    def reference_sensor_id(self):
        return self.__reference_sensor_id



class MeasureResult:

    def __init__(self, value, ambient):
        self.value = value
        self.ambient = ambient
        self.created_at = self.get_now()



    @staticmethod
    def get_now():
        return datetime.now()
