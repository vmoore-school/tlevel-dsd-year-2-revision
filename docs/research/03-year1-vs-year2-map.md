# 03 Year 1 to Year 2 Map

This guide **assumes the Year 1 Core is already known**: Core Papers 1 and 2 and the Employer Set
Project. This page shows which parts of the Core the Occupational Specialism builds on, and where the
gaps are. The status of every individual requirement is in [`CHECKLIST.md`](../../CHECKLIST.md).

## Already covered in Year 1 (revise, then apply)

| Year 1 Core | Where Year 2 uses it |
|---|---|
| 1.1 Computational thinking (decomposition, pattern recognition, abstraction) | Decomposing the brief in the Task 1 proposal |
| 1.2 Algorithms, flowcharts (BCS symbols), pseudocode | Task 1 algorithm designs |
| 1.3 Problem-solving approaches, root cause analysis | Supporting users, fixing issues (OS 8.4) |
| 2.x Python: data types, structures, I/O, files, functions, validation, robust code, debugging | Back-end language in Task 2 |
| 2.9 Naming conventions and code style | Coding conventions (OS 6.1, 8.3) |
| 2.12 Testing methods, test data (valid/invalid/boundary/erroneous), test plans | Test strategy and test log (OS 7) |
| 3.2 Emerging technologies (AI, generative AI, ML, IoT, XR, blockchain, quantum) | Research and proposals (OS 1.5) |
| 4.1 DPA 2018/UK GDPR, Computer Misuse Act, Equality Act, IP | Legal compliance (OS 2.1) |
| 4.2 Codes of conduct (BCS), W3C, WCAG, AUPs | Standards and ethics (OS 2.1) |
| 5.3 Risks to organisations | Risk management (OS 2.2) |
| 5.4 Change management: CAB, implementation methods, rollback, version control | Change management (OS 8.2) |
| 6.x Data: types, formats, models (hierarchical, network, relational), visualisation, APIs as an access method | Data design and dashboards (OS 4.3, 6.2, 6.3) |
| 7.x Hardware, OS, networks, virtualisation, cloud, resilience | Target platforms, deployment (OS 4.3, 6.4) |
| 8.x Threats, vulnerabilities, mitigation, CIA triad, encryption concepts, RBAC | Secure by design, secure coding (OS 1.4, 6.1) |
| ESP: Gantt chart, costings, debugging, pandas/matplotlib, evaluation | OS planning, testing, feedback analysis |

## Biggest gaps: new in Year 2

These have **no** Year 1 coverage and carry the most marks, so teach them first.

1. **A second language and web development**: HTML, CSS, JavaScript, plus SQL (or PHP or C#).
   The Core is Python-only. *(PO2: 39.6% of marks)*
2. **SQL and database design**: DDL/DML, ERDs, data dictionaries, normalisation to 3NF.
   The Core teaches the relational model in theory only.
3. **Back-end/server-side development**: routes, request/response, sessions, cookies, APIs, connecting
   to a database.
4. **Software methodologies**: Agile, Scaled Agile, Waterfall, RAD, Lean, user-centred design. Not in
   the Core at all.
5. **Requirements engineering**: functional and non-functional requirements, KPIs, user acceptance
   criteria, secure by design, spike testing.
6. **Design approaches**: OOP (classes, the four pillars, design patterns), TDD and BDD, functional
   programming, DFDs, UML.
7. **Version control in practice**: Git, branching, pull requests, GitFlow vs GitHub Flow.
8. **DevOps**: CI/CD pipelines, containers, the 12-factor app, deployment methods.
9. **UX/UI design**: wireframes, style guides, clickable prototypes, typography, colour and contrast.
10. **Generative AI for code**: prompting, reviewing, refining and evidencing AI-produced snippets
    (Task 1 Activity C).
11. **Research and feedback skills**: evaluating sources, surveys, interviews, observation, focus groups.
12. **User support and documentation**: release notes, user guides, FAQs, screencasts, API contracts.
13. **Extra legislation**: consumer protection, age ratings, advertising, gambling, territorial
    restrictions, ISO/IEC/IEEE 90003, software licences.

## Things that change name or emphasis

| Year 1 | Year 2 | Watch out for |
|---|---|---|
| "Boundary" test data | "Valid extreme" and "invalid extreme" test data | Use the OS terms in the test log |
| Knowing the theory of a test type | *Choosing and doing* the right test at the right SDLC stage | A justified test strategy |
| One language (Python) | At least two languages, working together | Front end and back end must integrate |
| Exam-length answers | Extended, justified project documents | Audience-appropriate writing |
| The ESP brief is given to you | You define the requirements yourself from the brief | Making requirements measurable and testable |
