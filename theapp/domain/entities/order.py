from ast import List
from theapp.domain.entities.product import Product
from theapp.domain.entities.user import User


class Order:
    def init(self, id: int, user: User, products: List[Product]):
        self.id = id
        self.user = user
        self.products = products