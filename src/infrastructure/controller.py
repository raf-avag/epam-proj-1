from abc import ABCMeta
from config import SLACK, EMAIL
from core.use_cases import NotifierUseCase
from infrastructure.services import LoggerService, EmailService, SlackService
from infrastructure.providers import (
    LoggerServiceProvider,
    EmailServiceProvider,
    SlackMessengerProvider,
)


class BaseController(metaclass=ABCMeta):
    def __init__(
        self,
        _slack_service,
        _email_service,
        _logger_service,
        _env_repo,
        _email_service_provider,
        _messenger_service_provider,
        _logger_service_provider,
    ) -> None:
        self._slack_service = _slack_service
        self._email_service = _email_service
        self._logger_service = _logger_service
        self._env_repo = _env_repo
        self._email_service_provider = _email_service_provider
        self._messenger_service_provider = _messenger_service_provider
        self._logger_service_provider = _logger_service_provider

    @property
    def logger_service(self) -> LoggerService:
        if self._logger_service is None:
            self._logger_service = LoggerService()
        return self._logger_service

    @property
    def logger_provider(self) -> LoggerServiceProvider:
        if self._logger_service_provider is None:
            self._logger_service_provider = LoggerServiceProvider(self.logger_service)
        return self._logger_service_provider

    @property
    def email_service(self) -> EmailService:
        if self._email_service is None:
            api_key = self._env_repo.get_one(EMAIL.api_key).value
            sercet_key = self._env_repo.get_one(EMAIL.secret_key).value
            self._email_service = EmailService(
                self.logger_provider, api_key, sercet_key
            )
        return self._email_service

    @property
    def email_provider(self) -> EmailServiceProvider:
        if self._email_service_provider is None:
            self._email_service_provider = EmailServiceProvider(
                self.logger_provider, self.email_service
            )
        return self._email_service_provider

    @property
    def slack_service(self) -> SlackService:
        if self._slack_service is None:
            token = self._env_repo.get_one(SLACK.bot).value
            self._slack_service = SlackService(self.logger_provider, token)
        return self._slack_service

    @property
    def slack_provider(self) -> SlackMessengerProvider:
        if self._messenger_service_provider is None:
            self._messenger_service_provider = SlackMessengerProvider(
                self.logger_provider, self.slack_service
            )
        return self._messenger_service_provider


class APIController(BaseController):
    def process_event(self, request):
        use_case = NotifierUseCase(request, self.slack_provider, self.email_provider)
        use_case.execute()
