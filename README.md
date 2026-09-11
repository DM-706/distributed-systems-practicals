# Distributed Systems Practicals

This repository contains the practical activities used throughout the Distributed Systems module.

The practicals begin with short Python and Git activities before moving into APIs, data exchange, persistence and other distributed-system challenges.

Most activities are completed individually in your own fork of this repository. Group assessment work is completed in a separate Azerbyte group repository.

## Repository Structure

Each individual practical is stored in a numbered topic folder:

```text
distributed-systems-practicals/
├── README.md
├── topic-01-launch-night/
├── topic-02-architecture/
├── topic-04-api-communication/
└── ...
```

Topic 3 does not have a folder in this repository. Its collaborative Git activity is completed inside your assigned Azerbyte group repository.

Open the `README.md` inside the relevant topic folder before changing any code. It contains the instructions, expected output, checks and Git commit points for that activity.

## Practical Activities

| Topic | Activity                                    | Main focus                                             | Location                  | Status                             |
| ----- | ------------------------------------------- | ------------------------------------------------------ | ------------------------- | ---------------------------------- |
| 1     | Launch Night                                | Python refresher and individual Git workflow           | Practical repository      | Available                          |
| 2     | Separating Launch Night                     | Python modules and separation of responsibilities      | Practical repository      | Available                          |
| 3     | Assessment Launch and Collaborative Git     | Shared repositories, contributions and merge conflicts | Azerbyte group repository | Available when groups are assigned |
| 4     | Your First Python API                       | HTTP requests, responses and Python APIs               | Practical repository      | Available                          |
| 5     | Data Representation and Persistence         | JSON rules, validation and SQLite storage              | To be added               | WIP                                |
| 6     | Middleware, Consistency and Synchronisation | Data rules, shared updates and middleware choices      | To be added               | WIP                                |
| 7     | Security in Distributed Systems             | Data protection, encryption and wider responsibilities | To be added               | WIP                                |
| 8     | Fault Tolerance and Availability            | Failure, retry and fallback behaviour                  | To be added               | WIP                                |
| 9     | Concurrency, Transactions and ACID          | Concurrent access and transaction handling             | To be added               | WIP                                |
| 10    | Evaluation and Report Support               | Evaluating distributed-system decisions and evidence   | To be added               | WIP                                |

**WIP** means that the activity is still being prepared. Do not begin a WIP activity until it has been introduced during the session.

## How to Complete a Practical

For each practical:

1. Open your existing cloned repository in Visual Studio Code.
2. Make sure your local copy is up to date.
3. Open the folder for the current topic.
4. Read the topic `README.md` before making any changes.
5. Work through the stages in order.
6. Run and test the program after each important change.
7. Commit your work at the points identified in the instructions.
8. Push your commits to your GitHub repository.
9. Refresh the repository on GitHub and check that your changes are visible.

You only need to fork and clone this repository once. Continue using the same local copy throughout the module.

## Getting New or Updated Practical Files

New practicals or corrections may be added to the original repository during the module.

Before updating your fork, make sure your existing work has been committed and pushed:

```bash
git status
git add .
git commit -m "Complete previous practical"
git push
```

If `git status` reports that there is nothing to commit, you can continue.

To receive updates:

1. Open your fork on GitHub.
2. Select **Sync fork**.
3. Select **Update branch**.
4. Open your existing repository in Visual Studio Code.
5. Run:

```bash
git pull
```

Do not clone the repository again. Updating the existing copy keeps your previous work and Git history together.

If Git reports a conflict or says that local changes would be overwritten, stop before forcing, discarding or deleting anything.

## Basic Git Workflow

Use `git status` regularly to see which files have changed:

```bash
git status
```

When you have completed and tested a meaningful change:

```bash
git add .
git commit -m "Describe the change"
git push
```

Your commit message should briefly explain what you changed. Avoid messages such as `work`, `update` or `finished`.

## Working Rules

* Work in your own fork of this repository.
* Use your existing cloned copy rather than cloning the repository again each week.
* Complete practicals in the order they are introduced.
* Read the instructions before changing the supplied files.
* Run and test your code before committing it.
* Make small, meaningful commits rather than one large commit at the end.
* Do not upload passwords, API keys, access tokens or personal information.
* Do not begin activities marked **WIP**.
* Stop before deleting files or discarding changes you do not recognise.

## Practical Work and Assessment

This repository contains individual learning activities designed to develop the knowledge and technical skills needed throughout the module.

It is separate from your Azerbyte group assessment repository. Do not store the assessed group prototype in this repository.

When a topic requires work inside the group repository, this will be stated clearly in the practical instructions.

## Getting Help

The instructions for creating a GitHub account, forking the repository and cloning it using Visual Studio Code are available on the **Getting Started with GitHub and Visual Studio Code** page on Canvas.

If something goes wrong:

* Keep the original error message visible.
* Run `git status` and read the output.
* Check that Visual Studio Code has opened the full repository folder.
* Check that you are editing the correct topic folder.
* Avoid deleting, forcing or cloning the repository again until the problem has been identified.
