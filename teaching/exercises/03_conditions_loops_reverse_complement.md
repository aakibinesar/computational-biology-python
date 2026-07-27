# Exercise 03: Conditions, Loops, and Reverse Complement

## Related Rosalind Problems

- `INI4` — Conditions and Loops
- `REVC` — Complementing a Strand of DNA

## Learning Goals

By the end of this exercise, learners should be able to:

- use `if` statements;
- use `for` loops;
- work with string characters;
- build a new string step by step;
- compute the reverse complement of a DNA sequence.

## Prerequisites

Learners should know:

- conditionals;
- loops;
- strings;
- dictionaries;
- indexing;
- reverse iteration.

## Task 1: Conditions and Loops

Write a loop that prints all odd numbers between two values.

Example:

```python
a = 10
b = 20
```

Expected output:

```text
11 13 15 17 19
```

## Starter Code

```python
a = 10
b = 20

for number in range(a, b + 1):
    if ...:
        print(number)
```

## Task 2: DNA Complement

Use the base-pairing rules:

| Base | Complement |
|---|---|
| A | T |
| T | A |
| C | G |
| G | C |

Given:

```python
dna = "AAAACCCGGT"
```

Create the complement:

```text
TTTTGGGCCA
```

## Task 3: Reverse Complement

Reverse the complement from Task 2.

Expected output:

```text
ACCGGGTTTT
```

## Starter Code

```python
dna = "AAAACCCGGT"

complement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
}

reverse_complement = ""

for base in reversed(dna):
    reverse_complement += ...

print(reverse_complement)
```

## Reflection Questions

1. Why do we reverse the sequence when computing reverse complement?
2. Why is a dictionary useful for complement rules?
3. How do loops help us process biological sequences?

## Repository Connection

This exercise connects to:

```text
notebooks/01_python_for_bioinformatics.ipynb
modules/03_biological_sequence_basics/
```

## Extension

Write a reusable function:

```python
def reverse_complement(dna: str) -> str:
    ...
```

Then test it on at least three DNA strings.
