from abc import ABCMeta, abstractmethod
from user.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod # 結局今後の用途も考えて abstractmethod にしました。(ただどっちでもいいかなとは未だに思ってます)
    def store(self, user: User) -> None:
        raise NotImplementedError()

    @abstractmethod
    def findById(self, id: str) -> User:
        raise NotImplementedError()
