#!/usr/bin/env python3

# execution of set actors
from Module.Actors.Actor import Actor
from Module.Actors.ActorState import ActorOffState
from Module.Actors.actor_settings import ACTOR_SETTINGS

for cycle in ACTOR_SETTINGS:
    _actor = Actor(cycle.GPIO, cycle.ON, cycle.OFF)
    _actorService = ActorOffState(_actor)
    _actorService.handle()
