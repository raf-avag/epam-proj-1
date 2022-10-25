from .interfaces import BaseUseCase
from src.infrastructure.serializers import EventSerializer
from src.infrastructure.config import SLACK
from flask import Response


class NotifierUseCase(BaseUseCase):
    def __init__(self, _data, _slack, _email):
        self._data = _data
        self._slack = _slack
        self._email = _email

    def execute(self):
        event = EventSerializer(self._data).deserialize()
        if event.event_type == "new_publication":
            self._slack.send_message(SLACK.channel, "Attention: there is " + str(event))
            return Response(status=202)
