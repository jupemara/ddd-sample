from abc import ABCMeta, abstractmethod
from user.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def store(self, user: User) -> None:
        raise NotImplementedError()
