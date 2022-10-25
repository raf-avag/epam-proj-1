from src.core.interfaces import (
    BaseEmailServiceProvider,
    BaseLoggerProvider,
    BaseMessengerServiceProvider,
)
from slack_sdk.errors import SlackApiError
import socket


class LoggerServiceProvider(BaseLoggerProvider):
    def __init__(self, LoggerService) -> None:
        self.logger = LoggerService.logger

    def error(self, message):
        return self.logger.error(message)

    def warning(self, message):
        return self.logger.warning(message)

    def info(self, message):
        return self.logger.info(message)

    def critical(self, message):
        return self.logger.critical(message)


class SlackMessengerProvider(BaseMessengerServiceProvider):
    def __init__(self, logger, service) -> None:
        self.logger = logger
        self.client = service.client
        # logger for initiation

    def send_message(self, channel, text):
        try:
            response = self.client.chat_postMessage(channel=channel, text=text)
            return response  # log
        except SlackApiError as e:
            return e.response["error"]  # log


class EmailServiceProvider(BaseEmailServiceProvider):
    def __init__(self, logger, service) -> None:
        self.logger = logger
        self.server = service.server

    def send_email(self, to, message):
        sender = {"Private Person <from@example.com>"}
        receiver = {to}
        try:
            response = self.server.sendmail(sender, receiver, message)
            return response  # log
        except socket.error as e:
            print("Could not connect to server ({0}): {1}".format(e.strerrror))
        finally:
            self.server.quit()
        # log
