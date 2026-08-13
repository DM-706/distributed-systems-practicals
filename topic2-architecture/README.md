# Topic 2: Separating Launch Night

In Topic 1, the Launch Night program stored and processed everything in one Python file. This works for a small program, but larger systems are easier to understand when different responsibilities are separated.

In this activity, you will compare two versions of the same program:

- a **centralised version**, where everything is contained in one file;
- a **modular version**, where responsibilities are separated into different Python files.

You will then add a new in-game mail component to the modular version.

> The modular version is not a distributed system yet. All of its files still run locally as part of one program. Later, we will make separate components communicate across a network using an API.

Work through each stage in order. Run the program after every important change.

## Before You Start

Open your existing `distributed-systems-practicals` repository in Visual Studio Code.

Open a terminal and run:

```bash
git status
```

Make sure that your previous work has already been committed before continuing.

## Stage 1: Run the Centralised Version

Open:

```text
topic-02-architecture/centralised/launch_night.py
```

The file contains functions for:

- logging in a player;
- selecting a realm;
- retrieving character information; and
- displaying the final output.

Run the program from the root of the practical repository:

```bash
python topic-02-architecture/centralised/launch_night.py
```

If `python` is not recognised, use:

```bash
py topic-02-architecture/centralised/launch_night.py
```

You should see:

```text
LAUNCH NIGHT
============
Player: GreenKnight
Login successful
Realm: Pyrewood Village
Character: Bronzebeard - Level 20 Warrior
```

Look through the file and find the function responsible for each line of output.

## Stage 2: Run the Modular Version

Open the `modular` folder. It contains:

```text
client.py
login_service.py
realm_service.py
character_service.py
```

Run:

```bash
python topic-02-architecture/modular/client.py
```

The output should be the same as the centralised version.

Open `client.py` and look at the first three lines:

```python
from login_service import login
from realm_service import select_realm
from character_service import get_character
```

These import functions from the other Python modules. The client can use those functions without containing all of their code.

Follow each imported function into its file and identify its responsibility.

## Stage 3: Compare the Versions

Open `comparison.md` and complete Questions 1–3.

Keep each answer brief. The important point is that you can explain how the program has been organised differently.

## Stage 4: Create the Mail Service

Inside the `modular` folder, create a new file named:

```text
mail_service.py
```

Add the following code:

```python
def get_mail():
    """Return the player's current in-game mail."""
    return ["Welcome to the realm!", "Your auction has sold!"]
```

Save the file.

The function returns a list containing two messages. At this point, the new module exists, but the client does not use it yet.

## Stage 5: Connect the Mail Service to the Client

Open `modular/client.py`.

Add this import beneath the existing imports:

```python
from mail_service import get_mail
```

Find this line:

```python
character = get_character("Bronzebeard")
```

Add the following line beneath it:

```python
mail = get_mail()
```

At the bottom of the file, add:

```python
print("Mail:")

for message in mail:
    print(f"- {message}")
```

Save the file and run the modular version again:

```bash
python topic-02-architecture/modular/client.py
```

The final part of the output should now be:

```text
Mail:
- Welcome to the realm!
- Your auction has sold!
```

If you receive an import error, check that:

- the file is named exactly `mail_service.py`;
- it is inside the `modular` folder; and
- the function is named exactly `get_mail`.

## Stage 6: Test the New Component

Open `mail_service.py` and add a third message to the list.

Run `client.py` again and check that the new message appears.

This shows that the mail component can be changed without editing the login, realm or character modules.

## Stage 7: Complete the Comparison

Return to `comparison.md` and complete the remaining questions.

Your answers should recognise that:

- the modular version separates responsibilities more clearly;
- separate Python files do not automatically create a distributed system; and
- network communication will be needed before these components can run separately.

## Stage 8: Commit and Push

Run:

```bash
git status
```

Check that your new and changed files are listed.

Then run:

```bash
git add topic-02-architecture
git commit -m "Add mail service component"
git push
```

Refresh your fork on GitHub and check that the new mail service, updated client and completed comparison are visible.

## Final Check

Before finishing, make sure that:

- both starter programs run;
- the modular version includes `mail_service.py`;
- all three mail messages are displayed;
- `comparison.md` is complete; and
- your changes have been committed and pushed.

## Optional Extension

Only begin this after completing the core activity.

Create an `auction_service.py` module containing a function that returns a list of auction items. Import it into `client.py` and display the items using a loop.

Make a separate commit describing your extension.
