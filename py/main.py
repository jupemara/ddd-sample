from usecase.user.register import UserRegisterUsecase
from adapter.repository.uuid_id_probider import Uuid
from adapter.repository.in_memory_user_repository import InMemory

if __name__ == "__main__":
    first_name = "John"
    last_name = "Smith"
    usecase = UserRegisterUsecase(
        Uuid(),
        InMemory()
    )
    usecase.execute(first_name, last_name)
