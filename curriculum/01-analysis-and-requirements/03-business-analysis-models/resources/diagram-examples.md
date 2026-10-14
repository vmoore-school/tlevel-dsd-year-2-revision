# Business Analysis Model Examples (Mermaid)

These render on GitHub and in most Markdown editors. Use them as starting points for the mock brief.

## Mind map
```mermaid
mindmap
  root((RCSC booking system))
    Members
      Book
      Cancel
      Reminders
    Coaches
      Registers
      Attendance
    Manager
      Dashboard
      Reports
    Legal
      UK GDPR
      Accessibility
```

## Activity diagram: book a session
```mermaid
flowchart TD
    start([Start]) --> login[Member logs in]
    login --> choose[Choose session]
    choose --> full{Spaces left?}
    full -- No --> wait[Offer waiting list] --> stop([End])
    full -- Yes --> confirm[Confirm booking]
    confirm --> email[Send confirmation email]
    email --> stop
```

## Process diagram (swimlanes): current paper process
```mermaid
flowchart LR
    subgraph Member
      a[Phones / WhatsApps club]
    end
    subgraph Staff
      b[Checks paper register] --> c{Space?}
      c -- Yes --> d[Writes name on register]
      c -- No --> e[Tells member it's full]
    end
    subgraph Coach
      f[Takes register to session]
    end
    a --> b
    d --> f
```

## Product road map
```mermaid
timeline
    title RCSC product road map
    v0.1 MVP : Online booking : Session list
    v0.2     : Login and roles : Coach registers
    v0.3     : Waiting list : Email reminders
    v1.0     : Manager dashboard : Online payment
```

## ERD (analysis level)
```mermaid
erDiagram
    MEMBER ||--o{ BOOKING : makes
    SESSION ||--o{ BOOKING : has
    COACH ||--o{ SESSION : runs
```
