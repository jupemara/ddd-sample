from domain.model.user.user import User
from domain.model.user.id import Id
import pytest

def test_user():
    cases = {
        "valid user": ["John", "Smith"],
        "valid user in Japanese": ["太郎", "山田"],
    }
    for k in cases:
        case = cases[k]
        user = User(
            Id(k),
            case[0],
            case[1],
        )
        assert user.id().value() == k
        assert user.name().first_name == case[0]
        assert user.name().last_name == case[1]

def test_user_error():
    cases = {
        "empty fist_name": ["", "non-empty"],
        "empty last_name": ["non-empty", ""],
    }
    for k in cases:
        with pytest.rases(AssertionError):
            case = cases[k]
            user = User(
                Id(k),
                case[0],
                case[1],
            )
