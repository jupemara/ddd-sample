from domain.model.user.user import User
from domain.model.user.repository import IUserRepository
from domain.model.user.id_provider import IIdProvider

class UserRegisterUsecase:
    def __init__(
        self,
        id_provider: IIdProvider,
        repository: IUserRepository,
    ) -> None:
        self.__id_provider = id_provider
        self.__repository = repository

    def execute(self, first_name: str, last_name: str) -> None:
        id = self.__id_provider.next_identity()
        user = User(id, first_name, last_name)
        self.__repository.store(user)
