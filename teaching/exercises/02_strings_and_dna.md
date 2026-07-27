# Exercise 02: Strings and DNA

## Related Rosalind Problems

- `INI3` — Strings and Lists
- `DNA` — Counting DNA Nucleotides
- `RNA` — Transcribing DNA into RNA

## Learning Goals

By the end of this exercise, learners should be able to:

- slice Python strings;
- count characters in a string;
- represent DNA as a string;
- count DNA nucleotides;
- transcribe DNA into RNA.

## Prerequisites

Learners should know:

- string indexing;
- string slicing;
- `len()`;
- `.count()`;
- `.replace()`.

## Task 1: String Slicing

Given:

```python
s = "HumptyDumptysatonawall"
```

Extract two substrings using index ranges.

Example pattern:

```python
first_word = s[a:b+1]
second_word = s[c:d+1]
```

Print both words separated by a space.

## Starter Code

```python
s = "HumptyDumptysatonawall"
a = 0
b = 5
c = 6
d = 11

first_word = ...
second_word = ...

print(first_word, second_word)
```

## Task 2: Count DNA Nucleotides

Given a DNA string:

```python
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
```

Count:

```text
A C G T
```

## Starter Code

```python
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

a_count = ...
c_count = ...
g_count = ...
t_count = ...

print(a_count, c_count, g_count, t_count)
```

## Task 3: Transcribe DNA to RNA

Replace every `T` with `U`.

## Starter Code

```python
dna = "GATGGAACTTGACTACGTAAATT"

rna = ...

print(rna)
```

## Expected Output

```text
GAUGGAACUUGACUACGUAAAUU
```

## Reflection Questions

1. Why can DNA be represented as a string?
2. Why is `.replace("T", "U")` enough for basic transcription?
3. How does nucleotide counting prepare us for k-mer counting?

## Repository Connection

This exercise connects to:

```text
notebooks/01_python_for_bioinformatics.ipynb
notebooks/03_sequence_statistics_motifs_kmers.ipynb
modules/03_biological_sequence_basics/
modules/04_sequence_statistics_motifs_kmers/
```

## Extension

Write two functions:

```python
def count_nucleotides(dna: str) -> dict[str, int]:
    ...

def transcribe(dna: str) -> str:
    ...
```
