from product import Product
from product_repository import ProductRepository

#### removeu o repository do construtor
class ProductService:
    def __init__(self) -> None:
      pass  

    def purchase(self, product: Product, quantity: int) -> float:
        return product.price * quantity
