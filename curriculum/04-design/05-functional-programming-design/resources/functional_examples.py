"""Functional programming features in Python (lesson 04.05). Run:  python functional_examples.py"""
from functools import partial, reduce

sessions = [
    {"name": "Junior Football", "sport": "Football", "booked": 14, "capacity": 20, "price": 5.0},
    {"name": "Netball Training", "sport": "Netball", "booked": 14, "capacity": 14, "price": 5.0},
    {"name": "Walking Football", "sport": "Football", "booked": 7, "capacity": 16, "price": 3.0},
]


# Recursion: a function that calls itself, with a base case that stops it
def total_bookings(items):
    if not items:                                   # base case
        return 0
    return items[0]["booked"] + total_bookings(items[1:])


# First-class functions: functions are values that can be stored and passed around
def is_full(session):
    return session["booked"] >= session["capacity"]


checks = {"full": is_full, "has_space": lambda s: not is_full(s)}   # anonymous function (lambda)


# Higher-order functions: take or return functions
def apply_discount(percent):
    """Returns a NEW function. The inner function 'closes over' percent (a closure)."""
    def discount(price):
        return round(price * (1 - percent / 100), 2)
    return discount


# Currying / partial application: fix some arguments now, supply the rest later
def revenue(price_multiplier, session):
    return session["booked"] * session["price"] * price_multiplier


if __name__ == "__main__":
    print("Total bookings (recursion):", total_bookings(sessions))

    print("Sessions with space (filter + first-class):",
          [s["name"] for s in filter(checks["has_space"], sessions)])

    print("Names in upper case (map + lambda):", list(map(lambda s: s["name"].upper(), sessions)))

    print("Sorted by spaces left (sorted with key):",
          [s["name"] for s in sorted(sessions, key=lambda s: s["capacity"] - s["booked"])])

    ten_percent_off = apply_discount(10)            # closure
    print("£5 with 10% off:", ten_percent_off(5.0))

    revenue_with_vat = partial(revenue, 1.2)        # partial application
    print("Revenue inc. VAT per session:", [round(revenue_with_vat(s), 2) for s in sessions])

    print("Total revenue (reduce):", reduce(lambda acc, s: acc + s["booked"] * s["price"], sessions, 0))

# Exercise: write the same five operations in JavaScript (Array.map, filter, sort, reduce, closures).
