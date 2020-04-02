from fastapi import HTTPException
from pydantic import BaseModel
from usecase.user.register import UserRegisterUsecase

class Request(BaseModel):
    first_name: str
    last_name: str

class UserRegisterController:
    def __init__(
        self,
        usecase: UserRegisterUsecase
    ) -> None:
      self.__usecase = usecase
    def handle(self, user: Request) -> None:
        try:
            self.__usecase.execute(user.first_name, user.last_name)
        except Exception:
            raise HTTPException(status_code=500, detail="internal server error")
