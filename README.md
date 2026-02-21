# openFDA API Exercise

## Overview
For this exercise, I explored the openFDA Drug Label API using Postman, curl, and Python requests. 

The goal was to:
- Practice API requests
- Use query parameters
- Implement pagination
- Handle empty results
- Extract useful fields from real JSON responses

---

## API Used
Endpoint:
https://api.fda.gov/drug/label.json

---

## Example Requests

Basic request:
GET https://api.fda.gov/drug/label.json?limit=1

Search by brand name:
GET https://api.fda.gov/drug/label.json?search=openfda.brand_name:"Advil"&limit=3

Pagination:
GET https://api.fda.gov/drug/label.json?search=openfda.brand_name:"Advil"&limit=3&skip=3

Empty test:
GET https://api.fda.gov/drug/label.json?search=openfda.brand_name:"THISSHOULDNOTEXIST12345"&limit=1

---

## User Story

As a user, I want to search for a medication by brand name and view key label information (generic name, purpose, and warnings) so that I can quickly understand what the drug is used for and any important safety warnings.

---

## Python Implementation

The script:
- Sends requests using the `requests` library
- Handles pagination using limit and skip
- Gracefully handles empty results
- Extracts:
  - brand_name
  - generic_name
  - purpose
  - warnings

To run:

```bash
python3 fda_test.py
```

## Exercise 2 - FastAPI User Service

Implemented a simple FastAPI application supporting:

- Create user
- Retrieve user by ID
- List users
- Return 409 if username exists
- Add text notes
- Read text notes

Tested using Swagger UI at /docs.
---

# Code Review Summary

## openFDA API Script

Strengths:
- Correct use of query parameters (`search`, `limit`, `skip`)
- Proper handling of pagination
- Graceful handling of empty or error responses
- Extracts relevant fields from nested JSON
- Clear structure and readable logic

The implementation focuses on clarity and correctness rather than over-engineering, which fits the scope of the exercise.

---

## FastAPI User Service

Strengths:
- Correct HTTP status codes:
  - `201` for successful creation
  - `409` for duplicate usernames
  - `404` for missing users
- Clean route structure
- Proper request body validation using Pydantic
- Simple in-memory data storage appropriate for a small exercise
- Successfully tested using Swagger UI

Overall, both exercises demonstrate correct API usage, backend logic implementation, and proper handling of common edge cases.
