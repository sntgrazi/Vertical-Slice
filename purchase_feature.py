from product_repository import ProductRepository
from user_interface_console import UserInterfaceConsole
from product import Product
from product_service import ProductService

# User interface virou purchase feature, chama repository, service e interfaceconsole

class PurchaseFeature:
    def __init__(self, product_repository: ProductRepository, product_service: ProductService, user_interface_console: UserInterfaceConsole) -> None:
        self.product_repository = product_repository
        self.product_service = product_service
        self.user_interface_console = user_interface_console
        
    def purchase(self) -> str:
        while (True):
            print(self.product_repository)
            
            input = self.user_interface_console.get_user_input_product_and_price()
            code = input[0]
            quantity = input[1]
            
            product: Product = None
            if (self.product_repository.check_if_product_exists(code)):
                product = self.product_repository.get(code)

            if (product == None):
                self.user_interface_console.print_result("Product not found...")
                break

            purchase_value = self.product_service.purchase(product, quantity)
            self.user_interface_console.print_result("Total: {0}".format(purchase_value))
