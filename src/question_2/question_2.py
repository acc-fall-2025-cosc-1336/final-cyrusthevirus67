class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    return [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]


def display_stock_list(stocks):
    print("Stock Report")
    print("Company\t\tSymbol")
    for stock in stocks:
        print(f"{stock.get_company_name()}\t{stock.get_symbol()}")


def main():
    stocks = get_stock_list()

    while True:
        print("\nMenu")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_stock_list(stocks)
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
