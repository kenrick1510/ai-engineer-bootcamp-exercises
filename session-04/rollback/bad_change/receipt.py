"""Receipt printer with discount codes, service fees and configurable formatting.

Run it from the top folder of the repository:
    python session-04/rollback/receipt.py
"""

import sys

from prices import CURRENCY_SYMBOL, PRICES, SERVICE_FEE, TAX_RATE, get_discount, get_price

SHOP_NAME = "My Shop"
ORDER = ["coffee", "bagel", "coffee", "juice"]
LINE_WIDTH = 24


class ReceiptLine:
    """One line of the receipt: a label and an amount."""

    def __init__(self, label, amount):
        self.label = label
        self.amount = amount

    def render(self):
        return f"  {self.label:<10} {CURRENCY_SYMBOL}{self.amount:>6.2f}"


class Receipt:
    """Collects lines and works out the totals."""

    def __init__(self, shop_name, discount_code=None):
        self.shop_name = shop_name
        self.discount_code = discount_code
        self.lines = []

    def add_item(self, item):
        self.lines.append(ReceiptLine(item, get_price(item)))

    def subtotal(self):
        return sum(line.amount for line in self.lines)

    def discount(self):
        return self.subtotal() * get_discount(self.discount_code)

    def tax(self):
        return (self.subtotal() - self.discount()) * TAX_RATE

    def total(self):
        return self.subtotal() - self.discount() + self.tax() + SERVICE_FEE

    def render(self):
        output = [self.shop_name, "-" * LINE_WIDTH]
        output += [line.render() for line in self.lines]
        output.append("-" * LINE_WIDTH)
        if self.discount_code:
            output.append(ReceiptLine("discount", -self.discount()).render())
        output.append(ReceiptLine("tax", self.tax()).render())
        output.append(ReceiptLine("service", SERVICE_FEE).render())
        output.append(ReceiptLine("TOTAL", self.total()).render())
        return "\n".join(output)


def main():
    discount_code = sys.argv[1] if len(sys.argv) > 1 else None
    receipt = Receipt(SHOP_NAME, discount_code)
    for item in ORDER:
        receipt.add_item(item)
    print(receipt.render())


if __name__ == "__main__":
    main()
