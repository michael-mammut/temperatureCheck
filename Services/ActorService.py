#!/usr/bin/env python3
from abc import ABC, abstractmethod
from datetime import datetime

import RPi.GPIO as GPIO


class AbstActor(ABC):

    def __init__(self, actor):
        self._actor = actor

    @abstractmethod
    def handle(self):
        pass

    def _set_actor_state(self, state):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._actor.gpio, GPIO.OUT)
        GPIO.setup(self._actor.gpio, state)
        GPIO.cleanup()

    def _turn_actor_on(self):
        now = datetime.now()
        return self._actor.on.hour >= now.hour and self._actor.on.minute >= now.minute


class ActorOnStateService(AbstActor):

    def __init__(self, actor):
        super().__init__(actor)

    def handle(self):
        if self._turn_actor_on():
            self._set_actor_state(GPIO.HIGH)
            return self
        else:
            return ActorOffStateService(self._actor)


class ActorOffStateService(AbstActor):

    def __init__(self, actor):
        super().__init__(actor)

    def handle(self):
        if not self._turn_actor_on():
            self._set_actor_state(GPIO.LOW)
            return self
        else:
            return ActorOnStateService(self._actor)
