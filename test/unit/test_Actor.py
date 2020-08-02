from datetime import datetime
from unittest import TestCase

from freezegun import freeze_time

from Module.Actors.Actor import Actor


class TestActor(TestCase):
    @freeze_time("2012-01-01 11:30")
    def test_set_actor_on(self):
            actor = Actor(7,  datetime.strptime('11:00', '%H:%M'),  datetime.strptime('12:00', '%H:%M'))
            self.assertTrue(actor.is_time_to_turn_on())

    @freeze_time("2012-01-01 10:30")
    def test_set_actor_off(self):
            actor = Actor(7,  datetime.strptime('11:00', '%H:%M'),  datetime.strptime('12:00', '%H:%M'))
            self.assertFalse(actor.is_time_to_turn_on())



