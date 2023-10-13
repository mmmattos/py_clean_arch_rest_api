from argparse import OPTIONAL
from theapp.domain.entities.user import User


class UserRepository:
	
	def get_user_by_email(self, email: str) -> OPTIONAL[User]:
		# Implementation to get user by email from database
		pass
	
	def save_user(self, user: User) -> User:
		# Implementation to save user to database
		pass 