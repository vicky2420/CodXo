from datetime import datetime
import sys

# Defining the CurrencyConverter class with mocked data
class CurrencyConverter:
    def __init__(self):
        # Mocked exchange rates 
        self.mocked_rates = {
            ('USD', 'EUR'): 0.9235,
            ('EUR', 'USD'): 1.0828,
            ('USD', 'GBP'): 0.768,
            ('GBP', 'USD'): 1.3021,
            # Add more pairs as needed
        }
        
        # Mocked historical rates for specific dates
        self.mocked_historical_rates = {
            ('USD', 'EUR', '2023-01-01'): 0.8802,
            ('EUR', 'USD', '2023-01-01'): 1.1360,
            # Add more pairs and dates as needed
        }
        
        # Mocked currency symbols
        self.mocked_symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            # Add more as needed
        }

        # Mocked currency names
        self.mocked_names = {
            'USD': 'United States Dollar',
            'EUR': 'Euro',
            'GBP': 'British Pound',
            # Add more as needed
        }
    
    # Method to convert currency using mocked data
    def convert_currency(self, amount, from_currency, to_currency):
        try:
            key = (from_currency, to_currency)
            if key in self.mocked_rates:
                rate = self.mocked_rates[key]
                converted_amount = amount * rate
                return converted_amount
            else:
                print(f"Error: Conversion rate not available for {from_currency} to {to_currency}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_currency_symbol(self, currency):
        try:
            if currency in self.mocked_symbols:
                return self.mocked_symbols[currency]
            else:
                print(f"Error: Symbol not available for {currency}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    # Method to get the name of a currency using mocked data
    def get_currency_name(self, currency):
        try:
            if currency in self.mocked_names:
                return self.mocked_names[currency]
            else:
                print(f"Error: Name not available for {currency}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    # Method to get the current exchange rate using mocked data
    def get_exchange_rate(self, from_currency, to_currency):
        try:
            key = (from_currency, to_currency)
            if key in self.mocked_rates:
                return self.mocked_rates[key]
            else:
                print(f"Error: Exchange rate not available for {from_currency} to {to_currency}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    # Method to get the historical exchange rate for a specific date using mocked data
    def get_historical_rate(self, from_currency, to_currency, date):
        try:
            key = (from_currency, to_currency, date.strftime('%Y-%m-%d'))
            if key in self.mocked_historical_rates:
                return self.mocked_historical_rates[key]
            else:
                print(f"Error: Historical rate not available for {from_currency} to {to_currency} on {date.strftime('%Y-%m-%d')}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

# Main function to run the currency converter program
def main():
    converter = CurrencyConverter()
    
    while True:
        print("\nCurrency Converter")
        print("1. Convert currency")
        print("2. Get exchange rate")
        print("3. Get historical rate")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount:"))
            from_currency = input("From currency (e.g. USD):").upper()
            to_currency = input("To currency (e.g. EUR):").upper()
            converted_amount = converter.convert_currency(amount, from_currency, to_currency)
            if converted_amount:
                from_symbol = converter.get_currency_symbol(from_currency) or from_currency
                to_symbol = converter.get_currency_symbol(to_currency) or to_currency
                print(f"{from_symbol}{amount} {from_currency} is equal to {to_symbol}{converted_amount} {to_currency}")

        elif choice == '2':
            from_currency = input("From currency (e.g. USD):").upper()
            to_currency = input("To currency (e.g. EUR):").upper()
            rate = converter.get_exchange_rate(from_currency, to_currency)
            if rate:
                print(f"The exchange rate from {from_currency} to {to_currency} is {rate}")

        elif choice == '3':
            from_currency = input("From currency (e.g. USD):").upper()
            to_currency = input("To currency (e.g. EUR):").upper()
            date_input = input("Enter date (YYYY-MM-DD):")
            try:
                date = datetime.strptime(date_input, "%Y-%m-%d")
                historical_rate = converter.get_historical_rate(from_currency, to_currency, date)
                if historical_rate:
                    print(f"The exchange rate on {date_input} from {from_currency} to {to_currency} was {historical_rate}")
            except ValueError:
                print("Invalid date format!. Please enter the date in YYYY-MM-DD format.")
        
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        
        else:
            print("Invalid choice!. Please choose a valid option.")

# Entry point of the  script
if __name__ == "__main__":
    main()
