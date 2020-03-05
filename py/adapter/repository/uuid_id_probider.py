from user.id_provider import IIdProvider
from user.id import Id
import uuid

class Uuid(IIdProvider):
    def next_identity(self) -> Id:
        generated = uuid.uuid4()
        return Id(str(generated))
