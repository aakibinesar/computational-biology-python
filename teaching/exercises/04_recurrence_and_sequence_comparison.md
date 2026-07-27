# Exercise 04: Recurrence and Sequence Comparison

## Related Rosalind Problems

- `FIB` — Rabbits and Recurrence Relations
- `HAMM` — Counting Point Mutations
- `SUBS` — Finding a Motif in DNA
- `FIBD` — Mortal Fibonacci Rabbits

## Learning Goals

By the end of this exercise, learners should be able to:

- implement a recurrence relation;
- compare two DNA strings;
- count Hamming distance;
- search for motifs;
- understand how recurrence can model biological counting problems.

## Prerequisites

Learners should know:

- loops;
- functions;
- lists;
- string indexing;
- conditional statements.

## Task 1: Fibonacci Rabbits

In the standard rabbit recurrence:

```text
F(n) = F(n-1) + F(n-2)
```

Write a function that returns the number of rabbit pairs after `n` months.

## Starter Code

```python
def fibonacci_rabbits(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")

    if n in (1, 2):
        return 1

    previous = 1
    current = 1

    for month in range(3, n + 1):
        previous, current = current, previous + current

    return current
```

## Task 2: Hamming Distance

Given two equal-length DNA strings, count how many positions are different.

Example:

```python
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
```

Expected output:

```text
7
```

## Starter Code

```python
def hamming_distance(s: str, t: str) -> int:
    if len(s) != len(t):
        raise ValueError("Sequences must have the same length")

    distance = 0

    for i in range(len(s)):
        if ...:
            distance += 1

    return distance
```

## Task 3: Motif Search

Find all one-based positions where a motif appears in a sequence.

Example:

```python
sequence = "GATATATGCATATACTT"
motif = "ATAT"
```

Expected output:

```text
2 4 10
```

## Starter Code

```python
def motif_positions(sequence: str, motif: str) -> list[int]:
    positions = []
    motif_length = len(motif)

    for i in range(len(sequence) - motif_length + 1):
        if ...:
            positions.append(i + 1)

    return positions
```

## Task 4: Mortal Fibonacci Rabbits

In mortal Fibonacci rabbits, each rabbit pair lives for `m` months.

Implement or study a recurrence-based solution where:

```python
n = number of months
m = lifespan in months
```

## Reflection Questions

1. How is recurrence different from ordinary looping?
2. Why does Hamming distance require equal-length strings?
3. Why does motif search use slicing?
4. Why is `FIBD` more realistic than `FIB`?

## Repository Connection

This exercise connects to:

```text
notebooks/02_algorithmic_foundations.ipynb
notebooks/03_sequence_statistics_motifs_kmers.ipynb
notebooks/04_dynamic_programming_alignment.ipynb
modules/05_genetics_and_probability/
modules/06_dynamic_programming_alignment/
```

## Extension

Compare `FIB` and `FIBD` outputs for the same `n`.

What changes when rabbit lifespan is limited?
