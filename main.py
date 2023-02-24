from product import Product
from product_repository import ProductRepository
from product_service import ProductService
from purchase_feature import PurchaseFeature
from user_interface_console import UserInterfaceConsole

product_repository = ProductRepository()

product1 = Product(1, "Hotdog", 4.00)
product2 = Product(2, "X-Salad", 4.50)
product3 = Product(3, "X-Bacon", 5.00)
product4 = Product(4, "Simple Toast", 2.00)
product5 = Product(5, "Refrigerant", 1.50)

product_repository.append(product1)
product_repository.append(product2)
product_repository.append(product3)
product_repository.append(product4)
product_repository.append(product5)

product_service = ProductService()
user_interface_console = UserInterfaceConsole()
purchase_feature = PurchaseFeature(product_repository, product_service, user_interface_console)

purchase_feature.purchase()