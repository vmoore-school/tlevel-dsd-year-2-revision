# BDD behaviour specification (Gherkin) for lesson 04.04.
# Structure: Title (Feature) -> Narrative (As a / I want / So that) -> Acceptance criteria (Scenarios).
# Tools such as behave (Python) or Cucumber (JS) can turn these into automated tests.

Feature: Book a training session
  As a club member
  I want to book a session online
  So that I don't have to phone the club

  Background:
    Given I am logged in as member 1
    And the session "Walking Football" has a capacity of 16

  Scenario: Booking a session with spaces
    Given "Walking Football" has 7 bookings
    When I book "Walking Football"
    Then I see the message "Booked!"
    And "Walking Football" has 8 bookings

  Scenario: Booking a full session
    Given "Walking Football" has 16 bookings
    When I book "Walking Football"
    Then I see the message "Session full"
    And I am offered a place on the waiting list

  Scenario: Booking the same session twice
    Given I have already booked "Walking Football"
    When I book "Walking Football"
    Then I see the message "Member already booked on this session"
