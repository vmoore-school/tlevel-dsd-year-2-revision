"""OOP concepts and three design patterns in Python (lesson 04.02). Run:  python oop_examples.py"""
from abc import ABC, abstractmethod


# ---------- Encapsulation and abstraction ----------
class Session:
    """A bookable session. Booking rules live inside the class (encapsulation)."""

    def __init__(self, name, capacity):
        self.name = name
        self._capacity = capacity     # leading underscore = internal; change it through methods only
        self._bookings = []

    @property
    def spaces_left(self):
        return self._capacity - len(self._bookings)

    def book(self, member):
        if self.spaces_left <= 0:
            raise ValueError(f"{self.name} is full")
        self._bookings.append(member)


# ---------- Inheritance and polymorphism ----------
class Member(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def price_for(self, base_price):
        """Each subclass decides its own price (polymorphism)."""


class AdultMember(Member):
    def price_for(self, base_price):
        return base_price


class JuniorMember(Member):
    def price_for(self, base_price):
        return round(base_price * 0.5, 2)


class ConcessionMember(Member):
    def price_for(self, base_price):
        return round(base_price * 0.7, 2)


# ---------- Creational pattern: Factory ----------
def member_factory(name, member_type):
    """Create the right Member subclass without the caller needing to know the classes."""
    types = {"adult": AdultMember, "junior": JuniorMember, "concession": ConcessionMember}
    return types[member_type](name)


# ---------- Behavioural pattern: Observer ----------
class BookingNotifier:
    """Subjects keep a list of observers and tell them when something happens."""

    def __init__(self):
        self._observers = []

    def subscribe(self, callback):
        self._observers.append(callback)

    def notify(self, message):
        for callback in self._observers:
            callback(message)


# ---------- Structural pattern: Adapter ----------
class LegacyPaymentSystem:
    def make_payment_in_pence(self, pence):
        return f"Paid {pence}p via legacy system"


class PaymentAdapter:
    """Lets new code call pay(pounds) while the old system expects pence."""

    def __init__(self, legacy):
        self._legacy = legacy

    def pay(self, pounds):
        return self._legacy.make_payment_in_pence(round(pounds * 100))


if __name__ == "__main__":
    netball = Session("Netball", capacity=2)
    notifier = BookingNotifier()
    notifier.subscribe(lambda msg: print("EMAIL:", msg))
    notifier.subscribe(lambda msg: print("LOG:  ", msg))

    payments = PaymentAdapter(LegacyPaymentSystem())
    for name, kind in [("Aisha", "adult"), ("Tom", "junior"), ("Mei", "concession")]:
        member = member_factory(name, kind)
        try:
            netball.book(member)
            price = member.price_for(5.00)
            notifier.notify(f"{member.name} booked {netball.name} for £{price:.2f}")
            print("      ", payments.pay(price))
        except ValueError as error:
            notifier.notify(f"{member.name} could not book: {error}")
