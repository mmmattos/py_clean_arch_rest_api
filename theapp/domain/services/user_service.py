from theapp.domain.entities.user import User
from theapp.domain.repositories.user_repository import UserRepository


class UserService:

    def init(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, email: str, password: str) -> User:
        # Implementation to create user and save to database
        pass

    def deactivate_user(self, user: User) -> None:
        user.deactivate()
        self.user_repository.save_user(user)