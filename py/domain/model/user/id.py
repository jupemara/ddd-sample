class Id:
    def __init__(self, value: str) -> None:
        # TODO: implement like every, some as util functions
        assert len(value) > 1, "assertion error"
        self.__value = value

    def value(self) -> str:
        return self.__value
