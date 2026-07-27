# Exercise 01: Python Variables and Arithmetic

## Related Rosalind Problem

- `INI2` — Variables and Some Arithmetic

## Learning Goals

By the end of this exercise, learners should be able to:

- assign values to variables;
- work with integers;
- use arithmetic operators;
- print output;
- write a simple Python script from a problem statement.

## Prerequisites

Learners should know:

- how to run a Python file;
- how to use variables;
- how to use `+`, `-`, `*`, `/`, and `**`;
- how to use `print()`.

## Task 1: Store Two Numbers

Create two variables:

```python
a = 3
b = 5
```

Print both values.

## Task 2: Square Each Number

Compute:

```text
a squared
b squared
```

Print both squared values.

## Task 3: Sum of Squares

Compute:

```text
a squared + b squared
```

This is the same idea used in Rosalind `INI2`.

## Starter Code

```python
a = 3
b = 5

a_squared = ...
b_squared = ...
answer = ...

print(answer)
```

## Expected Output for a = 3 and b = 5

```text
34
```

## Task 4: Try a Larger Example

Use:

```python
a = 989
b = 878
```

Print the sum of squares.

## Reflection Questions

1. Why do we use variables instead of typing the numbers directly everywhere?
2. What does the `**` operator do in Python?
3. Why is this a useful first programming exercise?

## Repository Connection

This exercise connects to:

```text
notebooks/01_python_for_bioinformatics.ipynb
modules/00_python_for_bioinformatics/
```

## Extension

Write a function:

```python
def sum_of_squares(a: int, b: int) -> int:
    ...
```

Then call the function with different values.
