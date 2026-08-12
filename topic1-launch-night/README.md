# Launch Night

A new online game has launched and thousands of players are trying to connect. The game uses several services, including a login service, a realm server and an Auction House.

In this activity, you will make some small changes to a working Python program. You will use Git to record those changes and push them to your own GitHub repository.

You do not need to complete the whole activity at once. Work through each stage in order and check that it works before moving on.

## Stage 1: Get Your Copy of the Project

Open the **Getting Started with GitHub** page on Canvas and follow it to:

1. Sign in to GitHub.
2. Fork this repository.
3. Check that the fork belongs to your account.
4. Clone your fork to the computer.
5. Open the cloned project.

Do not make changes until you have cloned **your fork**.

## Stage 2: Run the Starter Program

Open a terminal in the project folder and run:

```bash
python launch_night.py
```

If `python` is not recognised, try:

```bash
py launch_night.py
```

You should see:

```text
LAUNCH NIGHT SERVICE MONITOR
============================
Login Service: online
Realm Server: online
Auction House: offline

Offline services: 0
```

The program runs, but the final count is incorrect. There is one offline service, not zero. You will fix that later.

If the program does not run, stop here and check:

- the terminal is open in the cloned repository folder;
- the folder contains `launch_night.py`; and
- the command has been typed correctly.

## Stage 3: Look at the Service Data

Open `launch_night.py` and find `game_services` near the top.

The variable contains a **list**. Each item inside the list is a **dictionary** describing one game service.

For example:

```python
{"name": "Login Service", "status": "online"}
```

This dictionary has two keys:

- `name` stores the name of the service;
- `status` stores its current status.

## Stage 4: Add a New Service

Add the following dictionary beneath the Auction House entry:

```python
{"name": "In-game Mail", "status": "online"}
```

Remember to add a comma after the previous dictionary. The finished list should contain four services.

Run the program again. You should now see:

```text
In-game Mail: online
```

If you receive a syntax error, check the commas, quotation marks and brackets in the list.

## Stage 5: Make Your First Commit

You have completed a meaningful change, so record it using Git.

Run each command separately:

```bash
git status
```

`launch_night.py` should appear as a changed file.

```bash
git add launch_night.py
git commit -m "Add in-game mail service"
git push
```

Return to your repository on GitHub and refresh the page. Open `launch_night.py` and check that the new service appears there.

If the service appears on GitHub, you have successfully completed the full Git workflow.

## Stage 6: Fix the Offline Count

Find the `count_offline_services()` function. It currently returns `0` without checking the services.

Replace the `TODO` section with this code:

```python
offline_count = 0

for service in services:
    if service["status"] == "offline":
        offline_count += 1

return offline_count
```

This code:

1. Starts the count at zero.
2. Loops through every service.
3. Checks whether its status is `offline`.
4. Adds one to the count when an offline service is found.
5. Returns the final count.

Run the program again. The final line should now be:

```text
Offline services: 1
```

## Stage 7: Test Your Program

Change the Realm Server status from `online` to `offline` and run the program again.

Before running it, predict what the offline count should be.

If the function is working, the final count should now be `2`.

Return the Realm Server to `online` after completing the test.

## Stage 8: Commit and Push the Completed Program

Run:

```bash
git status
git add launch_night.py
git commit -m "Count offline game services"
git push
```

Refresh your repository on GitHub and check that both commits and the completed code are visible.

## Final Check

Before finishing, make sure that:

- the program displays four services;
- the Auction House is offline;
- the final offline count is `1`;
- your GitHub repository contains your changes; and
- you have made at least two commits.

## Short Question

Open `README.md` and replace the line below with one or two sentences explaining why Git is considered distributed.

### Why is Git distributed?

Write your answer here.

Commit and push your answer when it is complete.

## Optional Extension

Only move on to this section once the core activity is complete.

Update `display_services()` so that it displays a warning beneath any offline service. For example:

```text
Auction House: offline
  WARNING: This service is unavailable
```

Test the program with different service statuses and commit the extension separately.
