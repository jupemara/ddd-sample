import typing

def every(vs: typing.List[bool]) -> bool:
    for v in vs:
        if not v:
            return False
    return True

def some(vs: typing.List[bool]) -> bool:
    for v in vs:
        if v:
            return True
    return False
