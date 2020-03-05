from abc import ABCMeta, abstractclassmethod
from user.id import Id

class IIdProvider(metaclass=ABCMeta):
    @abstractclassmethod
    def next_identity(self) -> Id:
        raise NotImplementedError()
