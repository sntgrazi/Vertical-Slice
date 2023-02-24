class UserInterfaceConsole:
    def __init__(self) -> None:
        pass

    def get_user_input_product_and_price(self) -> list[int]:
        code_and_price = input("Enter the code and quantity of the product to be purchased: ").split()
        return [int(code_and_price[0]), int(code_and_price[1])]
        
    def print_result(self, result):
        print(result)
