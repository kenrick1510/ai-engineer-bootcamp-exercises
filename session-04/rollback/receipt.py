"""Print a receipt for a small order.

Run it from the top folder of the repository:
    python session-04/rollback/receipt.py
"""

from prices import PRICES, TAX_RATE

SHOP_NAME = "Corner Cafe"
ORDER = ["coffee", "bagel", "coffee", "juice"]


def subtotal(order):
    """Add up the price of every item in the order."""
    return sum(PRICES[item] for item in order)


def main():
    print(SHOP_NAME)
    for item in ORDER:
        print(f"  {item:<10} {PRICES[item]:>6.2f}")

    amount = subtotal(ORDER)
    tax = amount * TAX_RATE
    print(f"  {'tax':<10} {tax:>6.2f}")
    print(f"  {'TOTAL':<10} {amount + tax:>6.2f}")


if __name__ == "__main__":
    main()
