# Code Review Checklist

**Review type:** pair programming / informal walkthrough / formal inspection
**Author:** · **Reviewer(s):** · **Commit / PR:** · **Date:**

## Correctness
- [ ] Meets the requirement / user story
- [ ] Handles valid, extreme, invalid and erroneous input
- [ ] Errors are caught and handled, with helpful messages

## Security
- [ ] All input validated server-side; parameterised SQL
- [ ] Output encoded (no XSS); no secrets in code
- [ ] Access control checked on every protected route

## Maintainability
- [ ] Clear names that follow the conventions (PEP 8 / JS style guide)
- [ ] Functions do one thing; no copy-pasted blocks; no deep nesting
- [ ] Comments explain *why*; docstrings on public functions
- [ ] Constants rather than magic numbers; minimal globals

## Testing
- [ ] Tests added or updated, and passing
- [ ] Test log updated

## UX and accessibility (front end)
- [ ] Matches the wireframe and style guide; keyboard accessible; enough contrast

| # | File:line | Issue | Severity (major / minor / suggestion) | Agreed action |
|---|---|---|---|---|
