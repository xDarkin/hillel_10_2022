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

    def __add__(self, other):
        if self.currency.lower() != "usd" and other.currency.lower() == "usd":
            self.convert("USD")
            res_amount = self.amount + other.amount
        elif self.currency.lower() == "usd" and other.currency.lower() != "usd":
            other.convert("USD")
            res_amount = self.amount + other.amount
        elif self.currency.lower() == other.currency.lower():
            res_amount = self.amount + other.amount
        else:
            other.convert("USD")
            other.convert(self.currency)
            res_amount = self.amount + other.amount
        return res_amount, self.currency

    def __sub__(self, other):
        if self.currency.lower() != "usd" and other.currency.lower() == "usd":
            self.convert("USD")
            res_amount = self.amount - other.amount
        elif self.currency.lower() == "usd" and other.currency.lower() != "usd":
            other.convert("USD")
            res_amount = self.amount - other.amount
        elif self.currency.lower() == other.currency.lower():
            res_amount = self.amount - other.amount
        else:
            other.convert("USD")
            other.convert(self.currency)
            res_amount = self.amount - other.amount
        return res_amount, self.currency


if __name__ == "__main__":

    price_1 = Price(100, "EUR")
    price_2 = Price(100, "USD")
    price_3 = price_1.__add__(price_2)
    price_4 = Price(100, "EUR")
    price_5 = Price(100, "USD")
    price_6 = price_4.__sub__(price_5)

    print(f"Adding two prices gives {price_3[0]:.2f} {price_3[1]}")
    print(f"Subtracting two prices gives {price_6[0]:.2f} {price_6[1]}")
