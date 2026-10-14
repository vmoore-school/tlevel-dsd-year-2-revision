"""TDD kata: booking price calculator (lesson 04.04). Run:  python -m pytest tdd_kata.py

Red -> Green -> Refactor. Work through the tests ONE AT A TIME:
  1. Un-skip the next test.  2. Run it and watch it FAIL (red).
  3. Write the simplest code that makes it pass (green).  4. Refactor, keeping all tests green.

Rules to implement (one test each):
  - adult price is the base price
  - juniors pay half price
  - booking 5 or more sessions at once gives 10% off the total
  - prices are rounded to 2 decimal places
  - a negative number of sessions raises ValueError
"""
import pytest


def booking_price(base_price, sessions, member_type="adult"):
    # Start here. The first version only needs to pass the first test.
    return base_price * sessions


def test_adult_pays_base_price():
    assert booking_price(5.00, 1) == 5.00


@pytest.mark.skip(reason="TDD step 2: remove this line, watch it fail, then make it pass")
def test_junior_pays_half():
    assert booking_price(5.00, 1, "junior") == 2.50


@pytest.mark.skip(reason="TDD step 3")
def test_five_or_more_sessions_get_ten_percent_off():
    assert booking_price(5.00, 5) == 22.50


@pytest.mark.skip(reason="TDD step 4")
def test_rounds_to_two_decimal_places():
    assert booking_price(3.33, 5, "junior") == 7.49


@pytest.mark.skip(reason="TDD step 5")
def test_negative_sessions_rejected():
    with pytest.raises(ValueError):
        booking_price(5.00, -1)
