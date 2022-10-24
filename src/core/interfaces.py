from abc import ABCMeta, abstractmethod


class BaseMessengerServiceProvider(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "send_message")
            and callable(subclass.send_message)
            or NotImplemented
        )

    @abstractmethod
    def send_message(self):
        raise NotImplementedError


class BaseEmailServiceProvider(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "info") and callable(subclass.info) or NotImplemented

    @abstractmethod
    def send_email(self):
        raise NotImplementedError


class BaseLoggerProvider(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "info")
            and callable(subclass.info)
            and hasattr(subclass, "warning")
            and callable(subclass.warning)
            and hasattr(subclass, "error")
            and callable(subclass.error)
            and hasattr(subclass, "critical")
            and callable(subclass.critical)
            or NotImplemented
        )

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def warning(self):
        raise NotImplementedError

    @abstractmethod
    def error(self):
        raise NotImplementedError

    @abstractmethod
    def critical(self):
        raise NotImplementedError


class BaseUseCase(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "execute")
            and callable(subclass.execute)
            or NotImplemented
        )

    @abstractmethod
    def execute(self):
        raise NotImplementedError
