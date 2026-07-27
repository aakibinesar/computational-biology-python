# Exercise 06: Biopython Armory Workflows

## Related Rosalind Armory Problems

- `GBK` — GenBank Introduction
- `PTRA` — Protein Translation
- `TFSQ` — FASTQ format introduction
- `NEED` — Pairwise Global Alignment

## Learning Goals

By the end of this exercise, learners should be able to:

- understand how Biopython connects Python to biological databases and formats;
- describe Entrez-style search and fetch workflows;
- translate DNA sequences;
- understand FASTQ quality records;
- convert FASTQ-style data into FASTA-style records;
- understand how pairwise alignment workflows fit into bioinformatics practice.

## Prerequisites

Learners should know:

- FASTA format;
- FASTQ format;
- DNA and protein sequences;
- Python functions;
- basic Biopython usage.

## Task 1: Translation

Use Biopython to translate a DNA sequence into protein.

```python
from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
protein = dna.translate(to_stop=True)

print(protein)
```

## Task 2: FASTQ to FASTA

Given FASTQ records, write only the sequence ID and sequence in FASTA format.

## Example FASTQ

```text
@read_1
ACGTACGT
+
IIIIIIII
```

## Expected FASTA

```text
>read_1
ACGTACGT
```

## Starter Code

```python
from io import StringIO
from Bio import SeqIO

fastq_text = """@read_1
ACGTACGT
+
IIIIIIII
"""

records = SeqIO.parse(StringIO(fastq_text), "fastq")

for record in records:
    print(f">{record.id}")
    print(record.seq)
```

## Task 3: Entrez Workflow Description

Without running the code, describe the steps required to:

1. search GenBank for records matching an organism and date range;
2. fetch matching records;
3. count or inspect the results.

This mirrors the type of workflow used in Rosalind Armory `GBK`.

## Task 4: Alignment Workflow Description

Explain what a pairwise global alignment does.

Answer these questions:

1. What are the two input sequences?
2. What does the alignment score represent?
3. Why might a bioinformatician use global alignment?
4. How is this different from local alignment?

## Reflection Questions

1. Why are FASTQ files more information-rich than FASTA files?
2. Why should online database queries be handled carefully?
3. Why do translation problems sometimes require different genetic code tables?
4. Why are alignment tools useful even if we already know Python?

## Repository Connection

This exercise connects to:

```text
notebooks/06_biopython_ml_ready_features.ipynb
modules/12_practical_bioinformatics_biopython/
modules/13_ml_ready_bioinformatics_bridge/
```

## Extension

Build a small table from FASTQ records with:

- read ID;
- sequence;
- sequence length;
- average quality score.
