#!/usr/bin/env python3
from datetime import datetime

from RPi import GPIO


class Actor:
    def __init__(self, gpio, on: datetime, off: datetime):
        self.gpio = gpio
        self.on = on
        self.off = off

    def is_time_to_turn_on(self):
        now = datetime.now().time()
        on = self.on.time()
        off = self.off.time()
        return on < now < off

    def set_actor_on(self):
        if self.is_time_to_turn_on():
            self._set_actor_state(GPIO.LOW)
            return True
        else:
            self._set_actor_state(GPIO.HIGH)
            return False

    def _set_actor_state(self, state):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpio, GPIO.OUT)
        GPIO.setup(self.gpio, state)


