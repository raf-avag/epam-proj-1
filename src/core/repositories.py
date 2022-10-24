from abc import ABCMeta, abstractmethod


class BaseRepository(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get_one")
            and callable(subclass.get_one)
            or NotImplemented
        )

    @abstractmethod
    def get_one(self):
        raise NotImplementedError
