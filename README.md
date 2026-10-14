# T Level Digital Software Development: Year 2 Study Guide

A shareable, open template for studying and teaching **Year 2 of the T Level in Digital Software
Development (DSD)**: Pearson Technical Qualification **610/5801/4**, the Occupational Specialism.

It assumes **Year 1 (the Core: Paper 1, Paper 2 and the Employer Set Project) is already done**, and
covers everything needed for the **Occupational Specialism Project (OSP)**: a 50h 30m, 144-mark
project, taken March to May of Year 2, worth **50% of the T Level**.

> Based on the Pearson DSD specification v1.1 (August 2026). See [`docs/research/sources.md`](docs/research/sources.md).
> This guide is not affiliated with or endorsed by Pearson.

## Quick facts

| | |
|---|---|
| Assessment | One externally set, externally marked synoptic project in 4 tasks |
| Tasks | 1 Analyse & design · 2 Develop · 3a Gather feedback · 3b Evaluate (no internet) |
| Marks | 144: PO1 24 · **PO2 57** · PO3 18 · PO4 9 · PO5 18 · PO6 18 |
| Grade | Distinction / Merit / Pass |
| Languages | At least two of Python 3.10+, C#, SQL, JavaScript, PHP |
| Also needed | Industry placement of at least 315 hours |

## Start here

1. **Understand the assessment:** [`docs/research/02-osp-assessment-guide.md`](docs/research/02-osp-assessment-guide.md)
2. **See what's new compared with Year 1:** [`docs/research/03-year1-vs-year2-map.md`](docs/research/03-year1-vs-year2-map.md)
3. **Work through the curriculum:** [`curriculum/`](curriculum/README.md)
4. **Track progress:** [`CHECKLIST.md`](CHECKLIST.md) (298 requirements, each marked ✅ known / 🟨 partial / 🟥 new)
5. **Practise:** [`mock-briefs/`](mock-briefs/README.md) + [`starter-code/`](starter-code/README.md) + [`templates/`](templates/README.md)

## Repository layout

```
├── README.md                 you are here
├── CHECKLIST.md              master checklist: known / partial / new, plus a lesson build tracker
├── progress-tracker.csv      the same checklist as a spreadsheet (confidence ratings, notes)
├── CONTRIBUTING.md           how to use, extend and share this template
│
├── docs/research/            what the qualification and the OSP require (the research)
│   ├── 01-qualification-overview.md
│   ├── 02-osp-assessment-guide.md
│   ├── 03-year1-vs-year2-map.md
│   ├── 04-command-words-and-competencies.md
│   └── sources.md
│
├── curriculum/               WHAT TO TEACH: one folder per subject, one subfolder per lesson
│   ├── 00-osp-assessment-skills/        task walkthroughs, command words, time management
│   ├── 01-analysis-and-requirements/    SDLC, planning, BA models, roles, methodologies, requirements
│   ├── 02-legal-ethics-and-risk/        legislation, standards, licensing, risk
│   ├── 03-sources-and-feedback/         reliable sources, surveys, interviews, observation
│   ├── 04-design/                       OOP, TDD/BDD, FP, Git workflows, UX/UI, CMS, ERD/3NF
│   ├── 05-collaboration/                code review, pair programming, collaboration tools
│   ├── 06-implementation/               HTML/CSS/JS, back end, SQL, APIs, security, CI/CD, deployment, AI
│   ├── 07-testing/                      functional, non-functional, security, test data, automation
│   ├── 08-change-maintain-support/      maintenance types, change management, user support
│   └── 09-industry-placement/           placement requirements and logbook
│       └── <lesson>/README.md + resources/
│
├── templates/                blank documents for OSP evidence and lessons (copy before use)
├── sample-data/              fictional datasets (feedback, sales, support tickets, API JSON)
├── mock-briefs/              original OSP-style practice scenarios
├── starter-code/             working full-stack example (JS + Python/Flask + SQL) with tests, Docker, CI
├── student-workspace/        YOUR work: notes, lesson work, practice, mock OSP, placement
├── interactive-guide/        (planned) the interactive web version of this guide
└── tools/                    curriculum data and build script that generates the READMEs and checklist
```

Each lesson README lists: the spec reference, the Performance Outcomes and OSP tasks it supports, the
assumed Year 1 knowledge, **every requirement to teach with its status**, suggested activities,
resources and key terms.

## Teaching priorities

About **75% of the Year 2 requirements are new**. The Year 1 Core is Python-only and mostly theory.
Teach these first, because they carry the most marks and have the least Year 1 coverage:

1. A second language and web development (HTML/CSS/JavaScript), plus SQL: **PO2 is 40% of the marks**
2. Database design (ERD, data dictionary, 3NF) and back-end APIs
3. Requirements engineering (functional/non-functional, KPIs, acceptance criteria) and methodologies
4. Testing strategy, test logs and the OS test-data terms
5. Feedback gathering and evaluative writing for Tasks 3a/3b

## Licence

No licence has been chosen yet. Add one (e.g. CC BY 4.0 for content, MIT for code) before sharing, so
others know how they can reuse it.
