"""'Legacy' code for lesson 08.03 (Maintaining code in a team). It WORKS, but it is hard to maintain.

Task: refactor it (functions, constants, clear names, no repetition, comments, docstrings) while keeping
test_legacy_report.py passing. Then add an entry to a CHANGELOG.
"""


def r(d):
    t = 0
    o = ""
    for x in d:
        if x[1] == "Football":
            if x[2] > 0:
                t = t + x[2] * 5
                o = o + x[0] + ": " + str(x[2]) + " bookings, £" + str(x[2] * 5) + "\n"
            else:
                o = o + x[0] + ": no bookings\n"
        elif x[1] == "Netball":
            if x[2] > 0:
                t = t + x[2] * 5
                o = o + x[0] + ": " + str(x[2]) + " bookings, £" + str(x[2] * 5) + "\n"
            else:
                o = o + x[0] + ": no bookings\n"
        elif x[1] == "Cricket":
            if x[2] > 0:
                t = t + x[2] * 7
                o = o + x[0] + ": " + str(x[2]) + " bookings, £" + str(x[2] * 7) + "\n"
            else:
                o = o + x[0] + ": no bookings\n"
        else:
            if x[2] > 0:
                t = t + x[2] * 4
                o = o + x[0] + ": " + str(x[2]) + " bookings, £" + str(x[2] * 4) + "\n"
            else:
                o = o + x[0] + ": no bookings\n"
    o = o + "TOTAL: £" + str(t)
    return o
