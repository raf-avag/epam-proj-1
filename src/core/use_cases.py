from core.interfaces import BaseUseCase
from infrastructure.serializers import EventSerializer


class NotifierUseCase(BaseUseCase):
    def __init__(self, _data, _slack, _email):
        self._data = _data
        self._slack = _slack
        self._email = _email

    def execute(self):
        pass
