from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount


def main():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input(
                "Enter the source currency code (e.g., USD): ").upper()
            to_currency = input(
                "Enter the target currency code (e.g., EUR): ").upper()

            converted_amount = convert_currency(
                amount, from_currency, to_currency)

            print(
                f"\n{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        try_again = input(
            "\nDo you want to perform another conversion? (y/n): ").lower()
        if try_again != 'y':
            print("Exiting the Currency Converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
