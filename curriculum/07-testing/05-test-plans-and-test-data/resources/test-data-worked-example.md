# Test Data Worked Example

**Rule under test:** the number of people on a group booking must be a whole number from **1 to 20**.

| Test data type (spec term) | Meaning | Example values | Expected result |
|---|---|---|---|
| **Valid** | Normal data that should be accepted | 4, 10 | Accepted |
| **Valid extreme** | On the edge of the valid range, still accepted | 1, 20 | Accepted |
| **Invalid extreme** | Just outside the valid range | 0, 21 | Rejected: "Must be between 1 and 20" |
| **Invalid** | Right type, but breaks the rule | -5, 100 | Rejected |
| **Erroneous** | Wrong type or nonsense | "four", 2.5, blank, `<script>` | Rejected: "Enter a whole number" |

> Year 1 used the word **boundary** for what the OS calls valid and invalid **extreme** data. Use the
> OS terms in your OSP test log.

## A complete test-plan row
| ID | Purpose | Pre-requisite | Test data (type) | Expected | Actual | Pass/Fail | Changes made | Retest |
|---|---|---|---|---|---|---|---|---|
| T003 | Check the lower limit is enforced | Logged in; booking form open | 0 (invalid extreme) | Error shown; booking not saved | Booking saved with 0 people | Fail | Added `people >= 1` check on the server (commit `4f2a1c`) | T003a: Pass |

**Regression testing:** after the fix, re-run T001 to T010 to check nothing else broke.
