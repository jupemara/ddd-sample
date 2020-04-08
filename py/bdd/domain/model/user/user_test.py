from mamba import description, context, it
from domain.model.user.user import User
from domain.model.user.id import Id

with description('User') as self:
    with context('when create a new user with "John" as first name "Smith" as last name'):
        with it('has "John Smith" as name'):
            first_name = "John"
            last_name = "Smith"
            user = User(
                Id("test-user-id"),
                first_name,
                last_name,
            )
            assert user.name().first_name() == first_name
            assert user.name().last_name() == last_name
