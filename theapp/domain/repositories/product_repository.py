from typing import Optional
from theapp.domain.entities.product import Product


class ProductRepository:
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        # Implementation to get product by ID from db
        pass

    def save_product(self, product: Product) -> Product:
        # Implementation to save product to database
        pass