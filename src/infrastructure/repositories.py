from core.entities import EnvItemEntity
import pydotenv


class ConfigRepo:
    def __init__(self) -> None:
        self.repo = pydotenv.Environment()

    def get_one(self, key) -> EnvItemEntity:
        return EnvItemEntity(key, self.repo[key])
