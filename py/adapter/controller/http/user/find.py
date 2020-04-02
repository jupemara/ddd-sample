from fastapi import HTTPException
from usecase.user.find import UserFindUsecase

class UserFindController:
    def __init__(
        self,
        usecase: UserFindUsecase
    ) -> None:
      self.__usecase = usecase

    def handle(self, id: str): #ここreturnの型かけないのきついっすね
        dto = self.__usecase.execute(id)
        if dto is None:
            raise HTTPException(status_code=404, detail="user not found")
        return {
            'id': dto.id(),
            'first_name': dto.first_name(),
            'last_name': dto.last_name(),
        }
        # これ試してみたんですが、404のexcpetionに吸われました。。。
        # もしraiseしかできないのであれば、raiseでロジックを書くのはアンチパターンだと思います
        # これしかフレームワークないのであれば仕方ないのですが。。。
        # except Exception:
        #     raise HTTPException(status_code=500, detail="internal server error")
