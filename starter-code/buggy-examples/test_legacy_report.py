"""Characterisation tests: they pin down what legacy_report.r() does now, so a refactor can't change it."""
from legacy_report import r


def test_report():
    data = [("Junior Football", "Football", 10), ("Netball Training", "Netball", 0),
            ("Cricket Nets", "Cricket", 3), ("Fitness Circuit", "Fitness", 2)]
    assert r(data) == (
        "Junior Football: 10 bookings, £50\n"
        "Netball Training: no bookings\n"
        "Cricket Nets: 3 bookings, £21\n"
        "Fitness Circuit: 2 bookings, £8\n"
        "TOTAL: £79"
    )


def test_empty():
    assert r([]) == "TOTAL: £0"
