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
        result = on < now < off
        return result

    def set_actor_on(self):
        if self.is_time_to_turn_on():
            self._set_actor_state(GPIO.HIGH)
            return True
        else:
            self._set_actor_state(GPIO.LOW)
            return False

    def _set_actor_state(self, state):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpio, GPIO.OUT)
        GPIO.setup(self.gpio, state)
        GPIO.cleanup()
