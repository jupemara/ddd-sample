from fastapi import HTTPException
from pydantic import BaseModel
from usecase.user.register import UserRegisterUsecase

class User(BaseModel):
    first_name: str
    last_name: str

class UserRegisterController:
    def __init__(
        self,
        usecase: UserRegisterUsecase
    ) -> None:
      self.__usecase = usecase
    def handle(self, user: User) -> None:
        try:
            self.usecase.execute(user.first_name, user.last_name)
        except UserValidationError as e:
            if e.custom_eror_code == "9999"
                raise HTTPException(status_code=401, detail="validation error")
            raise HTTPException(status_code=500, detail="internal server error")
