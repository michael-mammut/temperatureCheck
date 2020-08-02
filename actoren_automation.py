#!/usr/bin/env python3

# execution of set actors
from Module.Actors.Actor import Actor
from Module.Actors.ActorState import ActorOffState, ActorOnState
from Module.Actors.actor_settings import ACTOR_SETTINGS

for cycle in ACTOR_SETTINGS:
    _actor = Actor(cycle.get("GPIO"), cycle.get("ON"), cycle.get("OFF"))
    _actor.set_actor_on()
