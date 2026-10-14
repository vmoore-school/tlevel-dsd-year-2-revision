# 02 OSP Assessment Guide: what each task asks for

The OSP is one scenario (a client brief) worked through four tasks. Evidence from one task **cannot be
changed** once you move on to the next, so quality has to be right first time.

> **Where this comes from.** The task structure, the PO weightings and the generative-AI rule come
> from the DSD specification (v1.1). Pearson had not published a DSD OS sample assessment when this
> was researched (October 2026). The activity-level detail, the evidence lists and the marker
> guidance below come from the DPDD OS sample assessment, which had the same four-task structure.
> Check Pearson's DSD page for a DSD sample and update this file when one appears.

## Overview

| Task | What you do | Key POs | Notes |
|---|---|---|---|
| **Task 1** Analysing a problem and designing a solution | Research, write a proposal, produce design documents, use generative AI for code snippets (Activity C) | PO1, PO2, PO5, PO6 | Research notes (facts and figures only) may be taken into sessions |
| **Task 2** Developing the solution | Build a working prototype in 2+ languages, test it iteratively, keep logs | PO2, PO3, PO4, PO6 | Access to your Task 1 work, but you cannot edit it |
| **Task 3a** Gathering feedback | Prepare demos for technical and non-technical audiences, plan and gather feedback | PO3, PO4, PO5 | Some unsupervised time to collect feedback from outside the centre |
| **Task 3b** Evaluating feedback | Write an evaluation of the prototype using the feedback | PO3, PO5, PO6 | **No internet**; short single session (2 hours in DPDD) |

Total supervised time is 50h 30m. Pearson sets the split between tasks and the dates for each series.
(In DPDD it was 20h / 30h / 15h / 2h over a 67-hour project. DSD is shorter, so expect less time per task.)

## Task 1: Analysing a problem and designing a solution

**Activity A: research.** Look into how digital solutions are used in the client's sector: hardware and
software in use, newly emerging technologies, how existing solutions meet different user needs, and
industry-specific guidelines and regulations. Notes taken into sessions must contain *facts and figures
only*, with no interpretation. They are submitted as an appendix.

**Activity A: proposal.** A justified proposal covering:
- the business context
- functional and non-functional requirements
- decomposition of the problems to be solved
- KPIs and user acceptance criteria
- a description of the proposed solution
- justification of how it meets client and user needs, how risks will be mitigated, and how legal and
  regulatory requirements will be addressed

**Activity B: design documents.**
- visual/interface designs (wireframes, style guide)
- data requirements (ERD, data dictionary, normalised design)
- algorithm designs: a selection of key problems (DPDD limited this to a maximum of five complex
  problems), as flowcharts or pseudocode
- a test strategy: the order in which components will be tested and the type of test for each
- the designs must let a third-party developer build the solution **and** let a non-technical client
  make decisions
- the solution must be big enough to need **two languages** (front end and back end)

**Activity C: generative AI (new in DSD).** Use a generative AI model (e.g. ChatGPT, Gemini) to create
**short snippets of code for specific functionality** that you then put into your larger solution.
- Show the prompts you used and the output you got.
- Review how well the output meets the need, then refine it.
- Never use AI to produce one overarching solution to the whole brief.

Use [`templates/osp-evidence/ai-prompt-log.md`](../../templates/osp-evidence/ai-prompt-log.md).

## Task 2: Developing the solution

Develop a functional prototype from your Task 1 designs. While you build, make sure you:
- write **secure code in at least two languages**
- gather and prepare assets, and record each one in an **assets log** (source, description/purpose,
  date retrieved)
- use and document **iterative testing** in a **test log** (inputs, calculations, validation, processes,
  with suitable test data and retests)
- document the iterative development process, including what changed and why
- produce code a third party can maintain
- deliver a high-quality user experience
- follow legal and regulatory guidelines and standards

Evidence (DPDD convention): key versions of the prototype, development documents, an assets log,
a test log, and the code as both PDF and .txt.

**What markers rewarded in DPDD Task 2:**
- modular, well-structured code using functions, procedures and classes
- server-side scripting with request/response, web service APIs, parsing JSON
- SQL used for both DDL and DML, with a related, multi-table data model
- meaningful indentation, local variables rather than globals, constants, a consistent style,
  defensive programming and good exception handling
- **avoiding** pages of nested IFs and copy-pasted procedural code
- UX that is useful, usable, desirable, findable, accessible and credible

## Task 3a: Gathering feedback

- Prepare demonstrations of the prototype for a **technical** audience (e.g. programmers) and a
  **non-technical** audience (e.g. client, users), using suitable tools such as screencasts or live demos.
- Write a **plan** for how you will gather feedback.
- Gather the feedback using the materials you made.
- Record it in a format you can analyse.

## Task 3b: Evaluating feedback

A written evaluation, produced **without internet access**, using only your design, your prototype and
your 3a feedback. It should cover:
- the effectiveness of the assets and content: why you chose them, why you rejected others, the
  validity and reliability of your sources, and their legal and ethical implications
- how well the solution meets the functional and non-functional requirements, the KPIs and the user
  acceptance criteria
- how the prototype could be developed further

## Rules that apply throughout

- Work independently. Cite anything that is not your own, including AI output.
- Tutors can give only limited general feedback (e.g. in Task 2, whether a design is appropriate or
  will work), and no guidance on how to improve your work.
- Work is stored securely between sessions. Nothing goes in or out without approval.
- File naming (DPDD convention): `TaskX_DocumentName_RegistrationNumber_Surname_Initial`.
  Practise it in [`student-workspace/mock-osp/`](../../student-workspace/mock-osp/README.md).
