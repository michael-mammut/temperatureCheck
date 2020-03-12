from w1thermsensor import W1ThermSensor
from pushbullet import PushBullet
from settings import PUSHBULLETTOKEN, TEMPERATURE_LIMITS, WATER_SENSOR_ID


def getTemperatureInCelsius():
    sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18S20, WATER_SENSOR_ID)
    return sensor.get_temperature(W1ThermSensor.DEGREES_C)


def pushNotification(temperature, title="no title"):
    message = "Wassertemp. liegt bei: " + str(temperature) + "°C"
    pb = PushBullet(PUSHBULLETTOKEN)
    pb.push_note(title, message)


temperature = getTemperatureInCelsius()

if temperature < TEMPERATURE_LIMITS["SETPOINT"]:
    pushNotification(temperature, "ACHTUNG! GERINGE TEMPERATUR")
elif TEMPERATURE_LIMITS["WARNING"] <= temperature < TEMPERATURE_LIMITS["ALERT"]:
    pushNotification(temperature, "ACHTUNG! WARME TEMPERATUR")
elif temperature >= TEMPERATURE_LIMITS["ALERT"]:
    pushNotification(temperature, "ACHTUNG! ZU WARM")
else:
    pushNotification(temperature, "INFO")
