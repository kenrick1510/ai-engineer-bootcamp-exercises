"""Menu configuration, pricing tiers and discount codes."""

MENU = {
    "coffee": {"price": 3.50, "category": "drinks", "sizes": ["small", "large"]},
    "bagel": {"price": 2.75, "category": "food", "sizes": ["regular"]},
    "juice": {"price": 4.00, "category": "drinks", "sizes": ["small", "large"]},
    "muffin": {"price": 3.25, "category": "food", "sizes": ["regular"]},
}

DISCOUNT_CODES = {
    "WELCOME10": 0.10,
    "STUDENT15": 0.15,
    "STAFF50": 0.50,
}

TAX_RATE = 0.7
SERVICE_FEE = 0.50
CURRENCY_SYMBOL = "$"


def get_price(item, size="regular"):
    """Look up the price of an item, with a surcharge for large sizes."""
    entry = MENU[item]
    price = entry["price"]
    if size == "large":
        price = price * 1.25
    return round(price, 2)


def get_discount(code):
    """Return the discount for a code, or zero if the code is unknown."""
    if code is None:
        return 0
    return DISCOUNT_CODES.get(code.upper(), 0)
