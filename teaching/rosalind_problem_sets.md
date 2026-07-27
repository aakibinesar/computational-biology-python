# Rosalind Problem Sets

This file documents the curated Rosalind problem sequence used in the original workshop and explains how those problems connect to the current repository.

The workshop did not use the entire Rosalind archive. It used selected problems to move learners gradually from basic Python into biological sequence analysis and Biopython workflows.

## Problem Progression

```text
Python basics
→ strings and arithmetic
→ loops and conditionals
→ DNA/RNA manipulation
→ recurrence
→ motif search
→ sequence comparison
→ Biopython Armory workflows
```

## Problems Used or Evidenced in the Workshop Materials

| Rosalind Track | Problem ID | Problem Title / Focus | Teaching Role |
|---|---|---|---|
| Python Village | `INI1` | Installing Python | first contact with Python and Rosalind |
| Python Village | `INI2` | Variables and Some Arithmetic | variables, arithmetic, simple input/output |
| Python Village | `INI3` | Strings and Lists | string slicing, indexing, basic data handling |
| Python Village | `INI4` | Conditions and Loops | conditionals and iteration |
| Bioinformatics Stronghold | `DNA` | Counting DNA Nucleotides | first biological string-counting task |
| Bioinformatics Stronghold | `RNA` | Transcribing DNA into RNA | string replacement as biological transformation |
| Bioinformatics Stronghold | `REVC` | Complementing a Strand of DNA | reverse complement logic |
| Bioinformatics Stronghold | `FIB` | Rabbits and Recurrence Relations | recurrence and biological counting |
| Bioinformatics Stronghold | `HAMM` | Counting Point Mutations | sequence comparison |
| Bioinformatics Stronghold | `SUBS` | Finding a Motif in DNA | substring search and motif positions |
| Bioinformatics Stronghold | `FIBD` | Mortal Fibonacci Rabbits | recurrence with lifespan constraints |
| Bioinformatics Armory | `INI` | Introduction to the Bioinformatics Armory | using Biopython for sequence tasks |
| Bioinformatics Armory | `FRMT` | Data Formats | FASTA retrieval and shortest-sequence selection |
| Bioinformatics Armory | `GBK` | GenBank Introduction | Entrez search and GenBank record counts |
| Bioinformatics Armory | `RVCO` | Complementing a Set of Sequences | reverse complement with Biopython |
| Bioinformatics Armory | `PTRA` | Protein Translation | translation and genetic code table selection |
| Bioinformatics Armory | `TFSQ` | FASTQ format introduction | FASTQ to FASTA conversion |
| Bioinformatics Armory | `NEED` | Pairwise Global Alignment | external alignment-tool workflow |

## Example Session B Problem Set

| Level | Track | Problem |
|---|---|---|
| Basic | Python Village | `INI2` — Variables and Some Arithmetic |
| Basic optional | Bioinformatics Stronghold | `DNA` — Counting DNA Nucleotides |
| Advanced | Python Village | `INI3` — Strings and Lists |
| Advanced optional | Bioinformatics Stronghold | `RNA` — Transcribing DNA into RNA |

This structure shows the teaching strategy clearly:

```text
Python skill first
→ biological version of the same skill
```

## Example Group-Based Problem Set

Another preserved problem set used this group progression:

```text
INI4 → REVC → FIB/HAMM/SUBS/FIBD
```

This connected loops and conditionals, reverse complement logic, recurrence, sequence comparison, motif search, and mortal Fibonacci recurrence.

## Repository Mapping

| Workshop Problem Area | Repository File |
|---|---|
| `INI1`–`INI4` | `notebooks/01_python_for_bioinformatics.ipynb` |
| `DNA`, `RNA`, `REVC` | `notebooks/01_python_for_bioinformatics.ipynb` |
| `FIB`, `FIBD` | `notebooks/02_algorithmic_foundations.ipynb`, `notebooks/04_dynamic_programming_alignment.ipynb` |
| `HAMM`, `SUBS` | `notebooks/03_sequence_statistics_motifs_kmers.ipynb` |
| `INI`, `FRMT`, `GBK`, `RVCO`, `PTRA`, `TFSQ` | `notebooks/06_biopython_ml_ready_features.ipynb` |
| feature-style extension | `mini_projects/ml_ready_sequence_features/` |

## Teaching Design Principle

The workshop used Rosalind not just as an assignment platform, but as a bridge between programming and biology.

```text
learn a Python concept
→ solve a simple programming task
→ apply it to a biological sequence task
→ generalize the idea into reusable code
```
