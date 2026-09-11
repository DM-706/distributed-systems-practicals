# Topic 4 Test Record

Complete this record after testing the API and client.

| Test | Expected result | Actual result | Pass/Fail |
|---|---|---|---|
| Request `/health` while the API is running | Status `200` and a JSON response showing the service is online |  |  |
| Request `/missing` while the API is running | Status `404` |  |  |
| Run the client while the API is stopped | A clear message explains that the API could not be reached |  |  |

## Short Questions

1. Why must `server.py` continue running while the client sends a request?


2. What is the difference between an HTTP status code and the JSON response body?


3. Why could this client continue to work if the API was later moved to another computer?


