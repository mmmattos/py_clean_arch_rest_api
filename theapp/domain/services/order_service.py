from ast import List
from theapp.domain.entities.order import Order
from theapp.domain.entities.user import User
from theapp.domain.repositories.order_repository import OrderRepository
from theapp.domain.repositories.product_repository import ProductRepository


class OrderService:

	def init(self, order_repository: OrderRepository, product_repository: ProductRepository):
		self.order_repository = order_repository
		self.product_repository = product_repository
		
	def create_order(self, user: User, product_ids: List[int]) -> Order:
    		# Implementation to create order and save to database
		pass

	def calculate_order_total(self, order: Order) -> float:
		# Implementation to calculate the total price of an order
		pass 