from fastapi import FastAPI
from usecase.user.register import UserRegisterUsecase
from adapter.controller.http.user.register import UserRegisterController
from adapter.controller.http.user.register import Request

from usecase.user.find import UserFindUsecase
from adapter.controller.http.user.find import UserFindController

from adapter.repository.uuid_id_probider import Uuid
from adapter.repository.in_memory_user_repository import InMemory

app = FastAPI()

findUsecase = UserFindUsecase(
    InMemory(),
)
findController = UserFindController(findUsecase)
registerUsecase = UserRegisterUsecase(
    Uuid(),
    InMemory(),
)
registerController = UserRegisterController(registerUsecase)

@app.get("/users/{user_id}")
async def find_user(user_id: str):
    findController.handle(user_id)

@app.post("/users/")
async def register_user(user: Request):
    registerController.handle(user)
