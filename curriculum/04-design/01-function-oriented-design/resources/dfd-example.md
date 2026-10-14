# Data Flow Diagram Example: RCSC booking system

DFD notation: **external entity** (rectangle), **process** (rounded box, numbered), **data store**
(open-ended box, D1...), **data flow** (labelled arrow). Every process must have at least one input
and one output.

## Level 0 (context diagram)
```mermaid
flowchart LR
    M[Member] -- booking request --> P0((0 RCSC Booking System))
    P0 -- confirmation / reminders --> M
    C[Coach] -- attendance --> P0
    P0 -- session register --> C
    MG[Manager] -- report request --> P0
    P0 -- dashboard data --> MG
```

## Level 1
```mermaid
flowchart LR
    M[Member] -- booking request --> P1(1 Validate & create booking)
    P1 -- confirmation --> M
    P1 -- new booking --> D2[(D2 Bookings)]
    D1[(D1 Sessions)] -- capacity & times --> P1
    D2 -- bookings for session --> P2(2 Produce register)
    P2 -- register --> C[Coach]
    C -- attendance --> P3(3 Record attendance)
    P3 -- attended flag --> D2
    D2 -- bookings & attendance --> P4(4 Calculate statistics)
    D1 -- sessions --> P4
    P4 -- dashboard data --> MG[Manager]
    D1 -- upcoming sessions --> P5(5 Send reminders)
    D3[(D3 Members)] -- email addresses --> P5
    P5 -- reminder email --> M
```

**Exercise:** add a level 1 process for the waiting list. What data stores does it read and write?
