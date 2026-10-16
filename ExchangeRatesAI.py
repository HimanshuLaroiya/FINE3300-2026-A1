import csv
from decimal import Decimal


class ExchangeRates:
    """Read and use the latest USD/CAD rate from a CSV file."""

    RATE_COLUMN = "FXAUSDCAD"

    def __init__(self, filename):
        # Load the exchange rate once when creating the object.
        self.exchange_rate = self._read_latest_rate(filename)

    def _read_latest_rate(self, filename):
        """Read the last available rate without loading the entire file."""

        latest_rate = None

        with open(
            filename, mode="r", newline="", encoding="utf-8-sig"
        ) as csv_file:

            reader = csv.DictReader(csv_file)

            # Confirm that the required column exists.
            if not reader.fieldnames or self.RATE_COLUMN not in reader.fieldnames:
                raise ValueError(
                    f"CSV must contain the '{self.RATE_COLUMN}' column."
                )

            # Process one row at a time to keep memory usage low.
            for row in reader:
                value = (row.get(self.RATE_COLUMN) or "").strip()

                # Ignore empty cells.
                if not value:
                    continue

                rate = Decimal(value)

                # Reject invalid numerical rates.
                if not rate.is_finite() or rate <= 0:
                    raise ValueError("The CSV contains an invalid exchange rate.")

                # The assignment specifies that the last row has the latest rate.
                latest_rate = rate

        if latest_rate is None:
            raise ValueError("No exchange rate was found in the CSV.")

        return latest_rate

    def convert(self, amount, from_currency, to_currency):
        """Convert between USD and CAD, returning an amount rounded to cents."""

        amount = Decimal(str(amount))
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        if from_currency == to_currency:
            result = amount

        elif from_currency == "USD" and to_currency == "CAD":
            result = amount * self.exchange_rate

        elif from_currency == "CAD" and to_currency == "USD":
            result = amount / self.exchange_rate

        else:
            raise ValueError("Currencies must be USD or CAD.")

        return result.quantize(Decimal("0.01"))


if __name__ == "__main__":

    # Ensure the CSV filename matches your actual file.
    csv_filename = "BankOfCanadaExchangeRate.2026.csv"

    exchange_rates = ExchangeRates(csv_filename)

    amount = Decimal(input("Enter amount: "))

    from_currency = input(
        "Enter source currency (USD or CAD): "
    ).strip().upper()

    to_currency = input(
        "Enter target currency (USD or CAD): "
    ).strip().upper()

    converted_amount = exchange_rates.convert(
        amount, from_currency, to_currency
    )

    print(
        f"{amount:,.2f} {from_currency} = "
        f"${converted_amount:,.2f} {to_currency}"
    )
