from fastapi import FastAPI
from adapter.controller.http.user.register import UserRegisterController
from adapter.controller.http.user.register import User
from usecase.user.register import UserRegisterUsecase
from adapter.repository.uuid_id_probider import Uuid
from adapter.repository.in_memory_user_repository import InMemory
from helper import registerController

app = FastAPI()

findUsecase = UserFindUsecase(
    InMemory()
)
findController = UserFindController(usecase)

@app.get("/users/{user_id}")
async def find_user(user_id: str):
    findController.handle(user_id)

@app.post("/users/")
async def register_user(user: User):
    registerController.handle(user)
