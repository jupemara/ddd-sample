from domain.model.user.user import User

class UserFindDto:
    def __init__(
        self,
        user: User,
    ) -> None:
        self.__id = id
        self.__first_name = user.name().first_name()
        self.__last_name = user.name().last_name()

    def id(self) -> str:
        return self.__id

    def first_name(self) -> str:
        return self.__first_name

    def last_name(self) -> str:
        return self.__last_name
