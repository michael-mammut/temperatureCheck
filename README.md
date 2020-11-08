# Temperature alert
Check the temperature of my aquarium and send me a push notification

### Version
v1.0.0

### Device
* Raspberry Pi 3
* Python

### Supported notification plattforms
* Telegram (default)
* Pushbullet

### APIs
* w1thermsensor (https://github.com/timofurrer/w1thermsensor)
* pushbullet (https://pypi.org/project/pushbullet.py/0.9.1/)
* telegram by http-Request

### Configuration
* Add the Token of your chosen notification plattform in `SETTINGS.tokens.py`
* Add your Sensor-IDs in `SETTINGS.temperature_settings.py`
* Adjust the temperature limits in `SETTINGS.temperature_settings.py`
* Install the used dependencies of the `reqirements.txt`

#### This is just a little project to fool around and spend time to escape the world and improve my skills in Python.

#### No warranty will be given regarding function or damage. Because it is just a project to improve software skills!!!