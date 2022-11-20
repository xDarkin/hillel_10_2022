from dataclasses import dataclass


@dataclass
class Price:
    amount: int
    currency: str

    def exchange_rate(self, target_currency: str):
        if self.currency.lower() == "uah" and target_currency.lower() == "usd":
            ex_rate = 0.025
        elif self.currency.lower() == "usd" and target_currency.lower() == "uah":
            ex_rate = 40
        elif self.currency.lower() == "eur" and target_currency.lower() == "usd":
            ex_rate = 1.1
        else:  # self.currency == "USD" and target_currency == "EUR":
            ex_rate = 0.9
        return ex_rate

    def convert(self, target_currency: str):
        ex_rate = self.exchange_rate(target_currency)
        self.amount = self.amount * ex_rate
        self.currency = target_currency
        return self.amount, self.currency


def add_prices(first_price: Price, other_price: Price):
    if first_price.currency.lower() != "usd" and other_price.currency.lower() == "usd":
        first_price.convert("USD")
        res_amount = first_price.amount + other_price.amount
    elif first_price.currency.lower() == "usd" and other_price.currency.lower() != "usd":
        other_price.convert("USD")
        res_amount = first_price.amount + other_price.amount
    elif first_price.currency.lower() == other_price.currency.lower():
        res_amount = first_price.amount + other_price.amount
    else:
        other_price.convert("USD")
        other_price.convert(first_price.currency)
        res_amount = first_price.amount + other_price.amount
    return res_amount, first_price.currency


def sub_prices(first_price: Price, other_price: Price):
    if first_price.currency.lower() != "usd" and other_price.currency.lower() == "usd":
        first_price.convert("USD")
        res_amount = first_price.amount - other_price.amount
    elif first_price.currency.lower() == "usd" and other_price.currency.lower() != "usd":
        other_price.convert("USD")
        res_amount = first_price.amount - other_price.amount
    elif first_price.currency.lower() == other_price.currency.lower():
        res_amount = first_price.amount - other_price.amount
    else:
        other_price.convert("USD")
        other_price.convert(first_price.currency)
        res_amount = first_price.amount - other_price.amount
    return res_amount, first_price.currency


if __name__ == "__main__":
    price_1 = Price(100, "EUR")
    price_2 = Price(100, "USD")
    adding = add_prices(price_1, price_2)
    subtraction = sub_prices(price_1, price_2)
    print(f"Adding two prices gives {adding[0]:.2f} {adding[1]}")
    print(f"Subtracting two prices gives {subtraction[0]:.2f} {subtraction[1]}")
