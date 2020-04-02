from domain.model.user.repository import IUserRepository
from usecase.user.dto import UserFindDto

class UserFindUsecase:
    def __init__(
        self,
        repository: IUserRepository,
    ) -> None:
        self.__repository = repository

    def execute(self, id: str) -> UserFindDto:
        user = self.__repository.findById(id)
        if user is None:
            return None
        return UserFindDto(user)
