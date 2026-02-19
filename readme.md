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
