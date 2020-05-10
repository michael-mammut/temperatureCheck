#!/usr/bin/env python3
from abc import ABC, abstractmethod


class AbstActor(ABC):

    def __init__(self, actor):
        self._actor = actor

    @abstractmethod
    def handle(self):
        pass


class ActorOnStateService(AbstActor):

    def __init__(self, actor):
        super().__init__(actor)

    def handle(self):
        if self._actor.set_actor_on():
            return self
        else:
            return ActorOffStateService(self._actor)


class ActorOffStateService(AbstActor):

    def __init__(self, actor):
        super().__init__(actor)

    def handle(self):
        if not self._actor.set_actor_on():
            return self
        else:
            return ActorOnStateService(self._actor)
