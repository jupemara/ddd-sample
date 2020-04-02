from user.repository import IUserRepository
from user.user import User

db = {}

class InMemory(IUserRepository):
    def store(self, user: User) -> None:
        db[user.id().value()] = user
    
    def findById(self, id: str) -> User:
        if id in db.keys():
            return db[id]
        return None
