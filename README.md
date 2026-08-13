# Distributed Systems Practicals

This repository contains the practical activities used throughout the Distributed Systems module.

Each topic has its own folder containing the files and instructions needed for that activity. The practicals begin with short Python and Git refreshers before moving towards communication between components, APIs, data exchange and other distributed-system challenges.

## Repository Structure

Each practical is stored in a numbered topic folder:

```text
distributed-systems-practicals/
├── README.md
├── topic-01-launch-night/
├── topic-02-architecture/
├── topic-03-api-communication/
└── ...
```

Open the `README.md` inside the relevant topic folder before changing any code. It contains the instructions, expected output, checks and Git commit points for that activity.

## Practical Activities

| Topic | Activity | Main focus | Status |
|---|---|---|---|
| 1 | Launch Night | Python refresher and individual Git workflow | Available |
| 2 | Separating Launch Night | Python modules, architecture and separation of responsibilities | Available |
| 3 | API Communication | HTTP, requests, responses and Python APIs | WIP |
| 4 | Data Representation and Interoperability | JSON and exchanging data between components | WIP |
| 5 | Security in Distributed Systems | Secure communication and encryption | WIP |
| 6 | Designing and Building a Prototype | Group prototype planning and development | WIP |
| 7 | Testing and Evaluating a Prototype | Testing components and evaluating design decisions | WIP |
| 8 | Fault Tolerance and Availability | Failure, retry and fallback behaviour | WIP |
| 9 | Concurrency, Transactions and ACID | Concurrent access and transaction handling | WIP |
| 10 | Consistency and Synchronisation | Conflicting data and synchronisation rules | WIP |

**WIP** means that the activity is still being prepared. Do not begin a WIP folder until it has been introduced in the session.

## How to Complete a Topic

For each practical:

1. Open your existing cloned repository in Visual Studio Code.
2. Open the folder for the current topic.
3. Read the topic `README.md` before making any changes.
4. Work through the stages in order.
5. Run and test the program after each important change.
6. Commit your work at the points identified in the instructions.
7. Push your commits to your GitHub repository.
8. Refresh your repository on GitHub and check that the changes are visible.

You only need to fork and clone this repository once. Continue using the same local copy throughout the module.

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

- Work in your own fork of the repository.
- Use your existing cloned copy rather than cloning the repository again each week.
- Complete practicals in the order they are introduced.
- Read the instructions before changing the supplied files.
- Run and test your code before committing it.
- Make small, meaningful commits rather than one large commit at the end.
- Do not upload passwords, API keys, access tokens or personal information.
- Do not begin folders marked **WIP**.

## Practical Work and Assessment

These practical activities are designed to help you develop the knowledge and technical skills needed throughout the module.

This repository is separate from the group assessment repository. Do not use this repository to store the group prototype unless you are specifically instructed to do so.

## Getting Help

The full instructions for creating a GitHub account, forking the repository and cloning it using Visual Studio Code are available on the **Getting Started with GitHub and Visual Studio Code** page on Canvas.

If something goes wrong:

- keep the original error message visible;
- run `git status` and read the output;
- check that Visual Studio Code has opened the full repository folder;
- check that you are editing the correct topic folder; and
- avoid deleting or cloning the repository again until the problem has been identified.
