from user.repository import IUserRepository
from user.user import User

db = {}

class InMemory(IUserRepository):
    def store(self, user: User) -> None:
        db[user.id().value()] = user
