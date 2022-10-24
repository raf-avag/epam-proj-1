import smtplib
import logging
from slack_sdk import WebClient
from config import EMAIL


class LoggerService:
    def __init__(self) -> None:
        self.logger = logging


class EmailService:
    def __init__(self, logger, api_key, secret_key) -> None:
        with smtplib.SMTP(EMAIL.link, EMAIL.port) as server:
            server.login(api_key, secret_key)
        self.server = server
        # log


class SlackService:
    def __init__(self, logger, token) -> None:
        self.__client = WebClient(token=token)
        # log

    @property
    def client(self):
        return self.__client
