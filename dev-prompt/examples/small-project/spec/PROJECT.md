# Pantry Log: Project specification

## Purpose
A personal command-line tool that records what is in a home pantry and lists items expiring soon, so food is used before it spoils.

## Users and platforms
One user (the author). Command-line on Linux and macOS. Maturity: personal application.

## Functional requirements
| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| R1 | M | Add an item with name, quantity, expiry date | `pantry add "rice" 2 2027-03-01` stores it; exit code 0 |
| R2 | M | List all items sorted by expiry | `pantry list` prints one line per item, earliest expiry first |
| R3 | M | List items expiring within N days | `pantry soon 7` prints only matching items; empty result prints "Nothing expiring" |
| R4 | S | Remove an item by name | `pantry remove "rice"` deletes it; unknown name exits non-zero with a message |
| W1 | W | Sync, accounts, barcode scanning, mobile app | Not built |

## Non-functional requirements
- Data stored in one local JSON file in the user's data directory; invalid or missing file is handled with a clear message, never a crash.
- No network access.

## Out of scope
Everything marked W1, a graphical interface, multi-user support.

## Stack (approved)
Python 3, standard library only, `pytest` for tests. No other dependencies without asking.

## Testing
Unit tests for R1–R4 including invalid dates and empty storage. Run `pytest` before reporting. Conventional approach, not TDD.
