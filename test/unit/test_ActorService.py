from datetime import datetime
from unittest import TestCase, mock

from Module.Actors.Actor import Actor
from Module.Actors.ActorState import ActorOnState, ActorOffState


class TestActorService(TestCase):

    def setUp(self) -> None:
        _on = datetime.strptime('11:00', '%H:%M')
        _off = datetime.strptime('12:00', '%H:%M')
        self._actor = Actor(7, _on, _off)

    def test_set_actor_from_off_on(self) -> None:
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=True):
            service = ActorOffState(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOnState)

    def test_set_actor_from_off_to_off(self) -> None:
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=False):
            service = ActorOffState(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffState)

    def test_set_actor_from_on_to_off(self) -> None:
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=False):
            service = ActorOnState(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffState)

    def test_set_actor_from_on_to_on(self) -> None:
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=True):
            service = ActorOnState(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOnState)

    def test_set_actor_some_changes(self) -> None:
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=False):
            service = ActorOffState(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffState)
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=True):
            service = service.handle()
            self.assertIsInstance(service, ActorOnState)
        with mock.patch.object(Actor, 'is_time_to_turn_on', return_value=False):
            service = service.handle()
            self.assertIsInstance(service, ActorOffState)