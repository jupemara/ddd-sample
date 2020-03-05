from domain.model.user.id import Id
from domain.model.user.name import Name

class User:
    def __init__(
        self,
        id: Id,
        first_name: str,
        last_name: str
    ) -> None:
        self.__id = id
        self.__name = Name(first_name, last_name)

    def id(self) -> Id:
        return self.__id

    def name(self) -> Name:
        return self.__name

    def change_name(self, first_name: str, last_name: str) -> None:
        # TODO: implement
        pass
