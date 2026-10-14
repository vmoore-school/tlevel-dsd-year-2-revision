# Requirements Specification: [Project name]

**Version:** 0.1 · **Author:** · **Date:** · **Client sign-off:**

## 1. Scope
_In scope / out of scope._

## 2. Secure by design
_How security is built in from the start (e.g. least privilege, validated input, encrypted data, secure defaults)._

## 3. Functional requirements
_What the system must DO. Cover inputs, data needed, processing, system logic, and deployment/usage platforms._

| ID | Requirement ("The system must...") | Inputs | Processing / logic | Outputs | Priority |
|---|---|---|---|---|---|

## 4. Non-functional requirements
_How well the system must perform. Make every one measurable._

| ID | Category | Requirement | Metric / target |
|---|---|---|---|
| NFR1 | Security | Passwords stored hashed with bcrypt | 100% of stored passwords hashed |
| NFR2 | Accessibility | Meets WCAG 2.2 AA | 0 AA failures in automated check |
| NFR3 | Responsiveness | Pages load quickly | < 2 s on 4G |
| NFR4 | Load handling | Supports concurrent users | 50 users, < 1% errors |
| NFR5 | Reliability | Available during opening hours | 99.5% uptime |
| NFR6 | Scalability | | |

## 5. User acceptance criteria
| ID | Given | When | Then | Linked requirement |
|---|---|---|---|---|

## 6. Constraints and assumptions
_Budget, time, platform, skills, legal._

## 7. Spike findings
_Any spike tests or proofs of concept used to clarify requirements, and what they showed._
