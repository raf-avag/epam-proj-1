class EnvItemEntity:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        if type(new_key) is not str:  # type checking for key property
            raise Exception("Key needs to be a str")
        self._key = new_key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) is not str:  # type checking for value property
            raise Exception("Value needs to be a str")
        self._value = new_value


class EventEntity:
    @property
    def EVENT_TYPES():
        return ("new_publication", "approved_publication")

    def __init__(self, event_type, body, to=None):
        if event_type not in self.EVENT_TYPES:
            raise ValueError("%s is not a valid event type." % event_type)
        self.event_type = event_type

        if type(body) is not str:
            raise ValueError("%s is not a valid body type." % type(body))
        self.body = body

        if type(to) not in (None, str):
            raise ValueError("%s is not a valid to type." % type(to))
        self.to = to

    def __str__(self) -> str:
        if self.event_type == "new_publication":
            return "A new publication"
        return "Approved publication"
