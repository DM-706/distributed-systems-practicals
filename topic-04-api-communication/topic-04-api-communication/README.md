# Topic 4: Your First Python API

In Topic 2, you separated a Python program into modules. Those modules still ran together because the client imported the other files directly.

In this practical, you will run two separate programs:

```text
Python client -> HTTP request -> Flask API
Python client <- JSON response <- Flask API
```

The starter files already contain a small `/health` endpoint. You will run and examine this before adding a second endpoint that returns information about a game realm.

## Before You Start

Open your existing clone of the Distributed Systems Practical Repository in Visual Studio Code.

Open a terminal and move into this folder:

```bash
cd topic-04-api-communication
```

Check that you are in the correct place:

```bash
git status
```

Do not create a new fork or clone the repository again.

## Stage 1: Prepare Python

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

If PowerShell prevents the environment from being activated, open a **Command Prompt** terminal in Visual Studio Code and run:

```bat
.venv\Scripts\activate.bat
```

### Checkpoint

Run:

```powershell
python -m pip show Flask
python -m pip show requests
```

Both packages should be listed.

## Stage 2: Run the API

Open `server.py` and find the route for `/health`.

Start the API:

```powershell
python server.py
```

The terminal should show that Flask is running at:

```text
http://127.0.0.1:5000
```

Keep this terminal open. The API must continue running while the client sends requests.

Open a browser and visit:

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "service": "realm-status",
  "status": "online"
}
```

### Checkpoint

Before continuing, make sure you can identify:

- The server address.
- The port number.
- The endpoint.
- The HTTP status code shown in the Flask terminal.
- The JSON returned by the API.

## Stage 3: Run the Client

Leave the API running and open a **second terminal** in Visual Studio Code.

Activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the client:

```powershell
python client.py
```

Expected output:

```text
Requesting: http://127.0.0.1:5000/health
Status code: 200
Response: {'service': 'realm-status', 'status': 'online'}
```

Open `client.py` and locate:

- The API's base address.
- The line that sends the GET request.
- The timeout.
- The code that reads the status code.
- The code that converts JSON into Python data.

## Stage 4: Add a Realm Endpoint

Return to `server.py`.

Add this route underneath the existing `/health` route and above the final `if` statement:

```python
@app.get("/realm")
def realm():
    return jsonify(
        {
            "name": "Emberfall",
            "status": "online",
            "players": 128,
        }
    ), 200
```

Save the file. Flask should restart automatically.

Visit the new endpoint in your browser:

```text
http://127.0.0.1:5000/realm
```

### Checkpoint

The response should contain the realm name, its status and the current player count.

## Stage 5: Update the Client

Open `client.py` and find:

```python
request_endpoint("/health")
```

Add another request underneath it:

```python
request_endpoint("/realm")
```

Run the client again:

```powershell
python client.py
```

The client should now receive successful responses from both endpoints.

## Stage 6: Test Unsuccessful Requests

Add this temporary request to the client:

```python
request_endpoint("/missing")
```

Run the client and observe the `404` response. Remove the temporary request after completing the test.

Next, stop the API using **Ctrl+C** and run the client again. It should display a clear message explaining that the API could not be reached.

Restart the API and confirm that the client works again.

Record all three tests in `test-record.md`:

- Successful `/health` request.
- Unknown `/missing` endpoint.
- Client request while the API is stopped.

## Stage 7: Explain What Happened

Complete the short questions at the bottom of `test-record.md`.

Your answers should explain the communication rather than simply stating that the code worked.

## Stage 8: Commit and Push

Stop the API using **Ctrl+C** and check your files:

```bash
git status
```

Commit and push your work:

```bash
git add .
git commit -m "Complete Topic 4 API practical"
git push
```

## Completion Check

Before finishing, make sure that:

- The `/health` and `/realm` endpoints return JSON.
- The client receives both successful responses.
- You tested a `404` response.
- You tested the client while the API was stopped.
- `test-record.md` is complete.
- Your changes have been committed and pushed.

## Further Challenge

Add a dynamic endpoint using this structure:

```text
/realm/<realm_name>
```

Return different JSON for at least two realm names and return a `404` response when the requested realm does not exist.

Update the client so the user can enter the name of the realm they want to check.

