# Python Exception Handling Exercises

This project contains five beginner Python exercises demonstrating exceptions, input validation, and file handling.

## Requirements

- Python 3

## Running the programs

Run a task from a terminal in the project directory:

```powershell
python Task1.py
```

Replace `Task1.py` with the task file you want to run.

## Exercises

| File | Description |
| --- | --- |
| `Task1.py` | Safe division: converts user input to numbers and handles invalid input and division by zero. |
| `Task2.py` | Bill calculator: totals valid non-negative numeric prices and skips invalid or negative values. |
| `Task3.py` | Age validator: uses a custom `AgeError` exception when an age is outside the range 1–120. |
| `Task4.py` | File reader: asks for a filename, displays up to the first three lines, and handles missing-file and permission errors. |
| `Task5.py` | Safe shopping cart: accepts prices until the user enters `q`, rejects invalid or negative prices, and prints the item count and total bill. |

## Usage notes

- For `Task4.py`, enter a readable text file's name or path when prompted.
- For `Task5.py`, enter one price at a time; enter `q` to finish.
