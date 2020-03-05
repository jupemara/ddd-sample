from util.utilhoge import every

class Name:
    def __init__(
        self,
        first_name: str,
        last_name: str
    ) -> None:
    # 氏名はそれぞれ、0文字以上、16文字以上
        assert every([
            len(first_name) >= 0,
            len(first_name) <= 16,
            len(last_name) >= 0,
            len(last_name) <= 16,
        ]), "assertion error"
        self.__first_name = first_name
        self.__last_name = last_name
    
    def first_name(self) -> str:
        return self.__first_name

    def last_name(self) -> str:
        return self.__last_name
