# Temperature alert
Check the temperature of my aquarium and send me notification.

### Version
v1.0.0

### Device
* Raspberry Pi 3
* Python

### Supported notification plattforms
* Telegram (default)
* Pushbullet

### APIs
* w1thermsensor - pip3 (https://github.com/timofurrer/w1thermsensor)
* pushbullet - pip3 (https://pypi.org/project/pushbullet.py/0.9.1/)
* telegram - http-Request (https://core.telegram.org/bots/api)

### Configuration
* Add the Token of your chosen notification plattform in `SETTINGS.tokens.py`
* Add your Sensor-IDs in `SETTINGS.temperature_settings.py`
* Adjust the temperature limits in `SETTINGS.temperature_settings.py`
* Install the used dependencies of the `reqirements.txt`
* Modify the logging folder
* Setup the execution (in my case i use three cron jobs)
`0 9   *   *   *    python3 /home/pi/Development/temperatureCheck/temperatureCheck.py`


#### No warranty will be given regarding function or damage. Because it is just a project to improve software skills!!!