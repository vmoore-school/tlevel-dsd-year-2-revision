# Mock Brief 01: Riverside Community Sports Club

> An **original practice brief** written in the style of an OSP set task. It is not a Pearson paper.
> The sample data, starter code and templates in this repo all use this scenario.

## Set task brief

The software development company you work for has won a contract with **Riverside Community Sports
Club (RCSC)**, a not-for-profit club with about 600 members aged 6 to 80, 15 volunteer coaches and
two part-time staff.

RCSC currently:
- takes session bookings by phone, WhatsApp groups and a paper register
- records payments in a spreadsheet, with card payments taken in person
- has no reliable record of attendance, so it cannot tell which sessions are worth running
- emails members using a personal email account

The club manager wants a digital solution that will:
- let members (or parents of junior members) book and cancel sessions online on any device
- let coaches see who is booked onto their sessions and take attendance
- give the manager information to support decisions about which sessions to run, and when
- store member data securely, including medical notes for some junior members

The club has asked members for ideas. Suggested features:
- a dashboard of attendance and income
- automatic reminders before sessions
- a waiting list for full sessions
- online payment
- an accessible design (several members have visual impairments, and some older members are not confident with technology)

## Task 1: Analysing the problem and designing a solution (practice)

**Activity A: research.** Look into how digital solutions are used by community sports clubs and leisure
providers: the hardware and software they use, emerging technologies, existing booking platforms and
how they meet different user needs, and relevant guidelines and legislation (e.g. UK GDPR for children's
and medical data, PECR, Equality Act, WCAG). Keep your notes to facts and figures only.

**Activity A: proposal.** Produce a proposal using
[`templates/osp-evidence/task1-proposal-template.md`](../templates/osp-evidence/task1-proposal-template.md).

**Activity B: design.** Produce interface designs, data requirements (ERD, data dictionary, normalised
to 3NF), algorithm designs for up to five key problems (e.g. booking with capacity check, waiting-list
promotion, reminder scheduling, dashboard aggregation, login with role-based access), and a test strategy.

**Activity C: generative AI.** Use a generative AI tool to produce code snippets for two specific
functions (e.g. "promote the first person on the waiting list when a booking is cancelled"). Record
your prompts, review the output and refine it.

## Task 2: Developing the solution (practice)

Build a functional prototype in **at least two languages**. You can extend
[`starter-code/`](../starter-code/README.md) or start from scratch. Keep a development log, a test log
and an assets log.

## Task 3a: Gathering feedback (practice)

Prepare a demo for the club manager (non-technical) and for a developer (technical). Gather feedback
and record it. To practise analysis without real users, use
[`sample-data/feedback-responses.csv`](../sample-data/feedback-responses.csv).

## Task 3b: Evaluating feedback (practice)

In 2 hours, with no internet, evaluate your prototype using
[`templates/osp-evidence/task3b-evaluation-template.md`](../templates/osp-evidence/task3b-evaluation-template.md).

## Suggested timings for a mock run (scale to the real window)

| Task | Practice time |
|---|---|
| Task 1 | 12 hours |
| Task 2 | 24 hours |
| Task 3a | 10 hours |
| Task 3b | 2 hours (no internet) |
