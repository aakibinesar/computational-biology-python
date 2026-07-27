# Exercise 05: Biopython Introduction

## Related Rosalind Armory Problems

- `INI` — Introduction to the Bioinformatics Armory
- `FRMT` — Data Formats

## Learning Goals

By the end of this exercise, learners should be able to:

- import Biopython modules;
- create a `Seq` object;
- compute complements and reverse complements;
- parse FASTA records;
- inspect sequence record IDs and sequences;
- select the shortest sequence from a group of records.

## Prerequisites

Learners should know:

- strings;
- functions;
- dictionaries or lists;
- basic file formats;
- FASTA format.

## Task 1: Create a Seq Object

```python
from Bio.Seq import Seq

dna = Seq("ATGCGATACGCTTGA")
```

Print:

- the sequence;
- the complement;
- the reverse complement.

## Starter Code

```python
from Bio.Seq import Seq

dna = Seq("ATGCGATACGCTTGA")

print(dna)
print(...)
print(...)
```

## Task 2: Parse FASTA Records

Use this FASTA text:

```text
>seq_1
ATGCGATACGCTTGA
>seq_2
ATGCCCGGGTTTAAA
>seq_3
TTTATGCGCGCGTAA
```

Parse the records using `SeqIO`.

## Starter Code

```python
from io import StringIO
from Bio import SeqIO

fasta_text = """>seq_1
ATGCGATACGCTTGA
>seq_2
ATGCCCGGGTTTAAA
>seq_3
TTTATGCGCGCGTAA
"""

records = list(SeqIO.parse(StringIO(fasta_text), "fasta"))

for record in records:
    print(record.id, record.seq, len(record.seq))
```

## Task 3: Find the Shortest Sequence

Write code that finds the shortest FASTA record.

## Starter Code

```python
shortest_record = min(records, key=lambda record: len(record.seq))

print(shortest_record.id)
print(shortest_record.seq)
```

## Reflection Questions

1. What does Biopython give us that plain Python strings do not?
2. What is the difference between a sequence and a sequence record?
3. Why is FASTA parsing useful in bioinformatics?

## Repository Connection

This exercise connects to:

```text
notebooks/06_biopython_ml_ready_features.ipynb
modules/12_practical_bioinformatics_biopython/
```

## Extension

Add a function:

```python
def shortest_fasta_record(records):
    ...
```

Return both the record ID and the sequence.
