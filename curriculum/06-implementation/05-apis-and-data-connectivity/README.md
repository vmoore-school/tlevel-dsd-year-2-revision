# 06.05 Connecting Code to Data Sources (APIs, JDBC, ODBC)

> **Subject:** Implementation (Two+ Languages)  
> **Spec reference:** OS 6.3  
> **Performance Outcomes:** PO2  
> **Used in OSP:** Task 1, Task 2  
> **Topic status:** 🟨 1 · 🟥 6

Key: ✅ known from Year 1 (revise only) · 🟨 partially known (extend) · 🟥 new (teach from scratch)

## Assumed prior knowledge (Year 1)

- Core 6.11 API as an access mechanism; Core 6.5 data formats (JSON, CSV, XML)

## What must be taught

| ID | Status | Requirement |
|---|---|---|
| 06.05.01 | 🟨 | APIs: request types/methods (GET, POST, PUT/PATCH, DELETE), endpoints |
| 06.05.02 | 🟥 | Retrieving, parsing and displaying JSON; API keys and keeping them secret |
| 06.05.03 | 🟥 | JDBC: core API, driver manager, connection, statement, prepared statement, result set |
| 06.05.04 | 🟥 | ODBC: application, driver manager, driver, data source |
| 06.05.05 | 🟥 | Connection methods: database name/data source, credentials, optional parameters |
| 06.05.06 | 🟥 | Extract, store, update and delete data from code (CRUD) |
| 06.05.07 | 🟥 | Connecting to network resources from within the IDE; selecting connection methods for the context |

## Suggested activities

- Call a public API (e.g. an open weather or postcodes API) and display results
- Compare a Python DB-API connection with a JDBC connection diagram

## Resources

- [api-response-example.json](../../../sample-data/api-response-example.json)
- [api_client_example.py](resources/api_client_example.py)

## Key terms

**REST**, **endpoint**, **JSON**, **API key**, **JDBC**, **ODBC**, **CRUD**

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
