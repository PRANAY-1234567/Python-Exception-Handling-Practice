# Python Exception Handling Practice

This repository contains basic Python programs created to practice **Exception Handling** using `try`, `except`, and `finally`.

The programs cover common Python exceptions such as `ZeroDivisionError`, `ValueError`, `IndexError`, `KeyError`, `FileNotFoundError`, and `NameError`.

## Topics Covered

* `try` block
* `except` block
* `finally` block
* Handling specific exceptions
* Displaying exception messages
* Handling multiple exceptions
* Basic file handling
* User input validation

## Programs

### 1. Handle ZeroDivisionError

Accepts two numbers and performs division. If the second number is `0`, the program handles the `ZeroDivisionError`.

**Exception:** `ZeroDivisionError`

### 2. Handle ValueError

Asks the user to enter an integer. If the user enters text instead of a number, the program handles the `ValueError`.

**Exception:** `ValueError`

### 3. Handle IndexError

Uses a list of numbers and asks for an index. If the entered index is outside the list range, the program handles the `IndexError`.

**Exception:** `IndexError`

### 4. Handle KeyError

Uses a student dictionary and asks the user to enter a key. If the key does not exist, the program handles the `KeyError`.

**Exception:** `KeyError`

### 5. Handle Multiple Exceptions

Accepts two inputs and performs division. The program handles:

* `ValueError` — when the user enters invalid input
* `ZeroDivisionError` — when the second number is zero

### 6. Display Exception Message

Attempts to convert `"abc"` into an integer. Since the conversion is invalid, the program catches the `ValueError` and displays the actual exception message.

### 7. Handle FileNotFoundError

Attempts to open and read `data.txt`.

If the file does not exist, the program handles `FileNotFoundError`.

A `finally` block is used to display:

```text
File operation completed
```

### 8. Login Program

Creates a simple login system using a predefined username and password.

The program:

1. Accepts username and password from the user.
2. Checks whether the credentials are correct.
3. Displays a success or invalid-login message.
4. Uses `finally` to display:

```text
Login process completed
```

### 9. Handle NameError

Creates a situation where an undefined variable is accessed.

The program catches the resulting `NameError` and displays an error message.

## Exception Handling Structure

The basic structure used in these programs is:

```python
try:
    # Code that may cause an exception

except ExceptionType:
    # Code to handle the exception

finally:
    # Code that always executes
```

## Technologies Used

* Python
* Python Exception Handling
* Basic File Handling
* User Input

## Learning Outcome

Through these exercises, I practiced identifying runtime errors and handling them properly instead of allowing the program to terminate unexpectedly.
