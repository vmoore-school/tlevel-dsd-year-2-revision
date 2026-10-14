# 06.06 Security Features in Code

> **Subject:** Implementation (Two+ Languages)  
> **Spec reference:** OS 6.1 (security features); 1.4 secure by design  
> **Performance Outcomes:** PO2, PO6  
> **Used in OSP:** Task 2  
> **Topic status:** 🟨 1 · 🟥 4

Key: ✅ known from Year 1 (revise only) · 🟨 partially known (extend) · 🟥 new (teach from scratch)

## Assumed prior knowledge (Year 1)

- Core 8 security: threats, mitigation, IAAA, encryption concepts, RBAC

## What must be taught

| ID | Status | Requirement |
|---|---|---|
| 06.06.01 | 🟥 | Controlling user access: authentication, password hashing (bcrypt/argon2), sessions/tokens, role-based authorisation in code |
| 06.06.02 | 🟨 | Encrypting data at rest and in transit (HTTPS/TLS) |
| 06.06.03 | 🟥 | Input validation & output encoding; preventing SQL injection and XSS; CSRF basics |
| 06.06.04 | 🟥 | Secrets management (environment variables, never commit keys) |
| 06.06.05 | 🟥 | OWASP Top 10 as a checklist |

## Suggested activities

- Fix the deliberately insecure login in the starter code's buggy-examples folder

## Resources

- [insecure_login.py](../../../starter-code/buggy-examples/insecure_login.py)

## Key terms

**hashing**, **salt**, **XSS**, **SQL injection**, **OWASP**, **least privilege**

## Lesson build status

_For whoever is writing this lesson. Tick these off in [CHECKLIST.md](../../../CHECKLIST.md)._

- Teaching notes
- Worked examples
- Practice activities
- Quiz / retrieval questions
- Resources complete
- Checked against spec

## Teaching notes

_To be written. Cover each requirement above; link worked examples and activities in `resources/`._
