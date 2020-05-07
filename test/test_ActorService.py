from datetime import datetime
from unittest import TestCase, mock

from Entities.Actor import Actor
from Services.ActorService import ActorOnStateService, ActorOffStateService


class TestActorService(TestCase):

    def setUp(self) -> None:
        _on = datetime.strptime('11:00', '%H:%M')
        _off = datetime.strptime('12:00', '%H:%M')
        self._actor = Actor(7, _on, _off)

    def test_set_actor_from_off_on(self) -> None:
        with mock.patch.object(ActorOffStateService, '_turnActorOn', return_value=True):
            service = ActorOffStateService(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOnStateService)

    def test_set_actor_from_off_to_off(self) -> None:
        with mock.patch.object(ActorOffStateService, '_turnActorOn', return_value=False):
            service = ActorOffStateService(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffStateService)

    def test_set_actor_from_on_to_off(self) -> None:
        with mock.patch.object(ActorOnStateService, '_turnActorOn', return_value=False):
            service = ActorOnStateService(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffStateService)

    def test_set_actor_from_on_to_on(self) -> None:
        with mock.patch.object(ActorOnStateService, '_turnActorOn', return_value=True):
            service = ActorOnStateService(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOnStateService)

    def test_set_actor_some_changes(self) -> None:
        with mock.patch.object(ActorOffStateService, '_turnActorOn', return_value=False):
            service = ActorOffStateService(self._actor)
            service = service.handle()
            self.assertIsInstance(service, ActorOffStateService)
        with mock.patch.object(ActorOffStateService, '_turnActorOn', return_value=True):
            service = service.handle()
            self.assertIsInstance(service, ActorOnStateService)
        with mock.patch.object(ActorOffStateService, '_turnActorOn', return_value=False):
            service = service.handle()
            self.assertIsInstance(service, ActorOffStateService)