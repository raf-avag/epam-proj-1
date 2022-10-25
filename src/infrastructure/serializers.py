from src.core.entities import EventEntity


class EventSerializer:
    def __init__(self, data) -> None:
        self.data = data

    def serialize(self) -> dict:
        return {
            "event_type": self.data.event_type,
            "body": self.data.body,
            "to": self.data.to,
        }

    def deserialize(self) -> EventEntity:
        return EventEntity(self.data["event_type"], self.data["body"], self.data["to"])
