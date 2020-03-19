#!/usr/bin/env python3
from w1thermsensor import W1ThermSensor
from pushbullet import PushBullet
from settings import PUSHBULLETTOKEN, TEMPERATURE_LIMITS, WATER_SENSOR_ID, AMBIETEN_SENSOR_ID


def getTemperatureInCelsius(id):
    sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, id)
    return sensor.get_temperature(W1ThermSensor.DEGREES_C)


def pushNotification(waterTemperature, ambientTemperature, title="no title"):
    message = "Wassertemp. liegt bei: " + str(waterTemperature) + "°C. Raumtemperatur bei " + str(ambientTemperature) + "°C"
    pb = PushBullet(PUSHBULLETTOKEN)
    pb.push_note(title, message)

ambientTemperature = getTemperatureInCelsius(AMBIETEN_SENSOR_ID)
temperature = getTemperatureInCelsius(WATER_SENSOR_ID)

if temperature < TEMPERATURE_LIMITS["SETPOINT"]:
    pushNotification(temperature, ambientTemperature, "ACHTUNG! GERINGE TEMPERATUR")
elif TEMPERATURE_LIMITS["WARNING"] <= temperature < TEMPERATURE_LIMITS["ALERT"]:
    pushNotification(temperature, ambientTemperature, "ACHTUNG! WARME TEMPERATUR")
elif temperature >= TEMPERATURE_LIMITS["ALERT"]:
    pushNotification(temperature, ambientTemperature, "ACHTUNG! ZU WARM")
else:
    pushNotification(temperature, ambientTemperature, "INFO")
