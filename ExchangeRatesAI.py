import csv


class ExchangeRates:
    def __init__(self, filename):
        self.exchange_rate = self.read_exchange_rate(filename)

    def read_exchange_rate(self, filename):
        """
        Reads the latest USD/CAD exchange rate from the CSV file.
        Assumes the last row contains the latest exchange rate.
        """
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            last_row = None
            for row in reader:
                last_row = row

        return float(last_row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        """
        Converts between USD and CAD.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.exchange_rate

        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.exchange_rate

        elif from_currency == to_currency:
            return amount

        else:
            raise ValueError("Unsupported currency conversion.")


def main():
    exchange_rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter amount: "))
    from_currency = input("Enter FROM currency (USD or CAD): ")
    to_currency = input("Enter TO currency (USD or CAD): ")

    converted_amount = exchange_rates.convert(
        amount,
        from_currency,
        to_currency
    )

    print(
        f"${converted_amount:,.2f} {to_currency.upper()}"
    )


if __name__ == "__main__":
    main()