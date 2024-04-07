import abc

from src.workflows.config import settings


class BaseFetcher(abc.ABC):
    """Абстрактный класс для извлечения данных из хранилища данных.

    Позволяет получать пакетами данные из выбранного источника хранения данных.
    Способ получения данных может варироваться от базы данных с которой мы работаем
    """

    @abc.abstractmethod
    def fetch_many(
        self, query: dict = None, size: int = settings.batch_size, *args, **kwargs
    ):
        pass
