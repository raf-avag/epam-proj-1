from .interfaces import BaseUseCase
from src.infrastructure.serializers import EventSerializer
from src.infrastructure.config import SLACK


class NotifierUseCase(BaseUseCase):
    def __init__(self, _data, _slack, _email):
        self._data = _data
        self._slack = _slack
        self._email = _email

    def execute(self):
        event = EventSerializer(self._data).deserialize
        if event.event_type == "new_publication":
            self._slack.send_message(SLACK.channel, event)
