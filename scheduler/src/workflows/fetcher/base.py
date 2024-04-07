from abc import ABC, abstractmethod


class DatabaseABC(ABC):
    @abstractmethod
    def connect(self, **kwargs):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def find(self, *args, **kwargs):
        ...

    @abstractmethod
    def insert(self, *args, **kwargs):
        ...

    @abstractmethod
    def get_all(self, *args, **kwargs):
        ...
