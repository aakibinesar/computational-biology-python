# Curriculum Map

This curriculum map organizes 202 solved Rosalind problems into a teaching-oriented structure connecting Python programming, core algorithms, computational biology, Biopython workflows, and ML-ready biological sequence analysis.

The original solutions are preserved by Rosalind track inside `original_rosalind_tracks/`. This curriculum reorganizes them conceptually so that learners can move from foundational computer science skills toward applied bioinformatics problems.

## Curriculum Design Principles

1. Python and algorithmic foundations come first.
2. Biological sequence analysis is introduced after basic string/file handling.
3. Algorithmic Heights problems are connected to biological applications instead of being treated separately.
4. Bioinformatics Stronghold, Armory, and Textbook Track problems are grouped by concept.
5. Each module identifies prerequisite problems, applied problems, teaching outputs, and selected problems for deeper explanation.

## Treatment Labels

- **Fully explained** — receives detailed teaching notes, algorithm explanation, code walkthrough, and complexity discussion.
- **Worked example** — receives clean code and a short explanation.
- **Archive solution** — preserved as a solved problem but not expanded in detail.
- **Capstone** — used in a larger cross-module project or notebook.

# Module Structure

## Module 00: Python for Bioinformatics

### Teaching Purpose

This module introduces Python as a practical language for biological sequence analysis. It covers strings, lists, dictionaries, arithmetic, loops, and file input/output.

### Rosalind Track Connection

- Python Village

### Problems Used

- INI1
- INI2
- INI3
- INI4
- INI5
- INI6

### Concepts

- Python syntax
- String manipulation
- Lists and dictionaries
- Basic arithmetic
- File reading
- Simple text processing

### Connected Bioinformatics Applications

These Python skills support later problems such as:

- DNA
- RNA
- REVC
- GC
- SUBS
- CONS
- FASTA/FASTQ parsing problems from Bioinformatics Armory

### Suggested Treatment

| Problem | Role |
|---|---|
| INI1 | Worked example |
| INI2 | Worked example |
| INI3 | Fully explained |
| INI4 | Worked example |
| INI5 | Fully explained |
| INI6 | Fully explained |

### Teaching Output

- Short lesson note
- Beginner notebook
- Exercise sheet

## Module 01: Algorithmic Foundations — Arrays, Sorting, and Searching

### Teaching Purpose

This module introduces core algorithmic tools that later support computational biology workflows, especially efficient sequence processing, k-mer counting, feature extraction, sorting, indexing, and recurrence-based reasoning.

### Rosalind Track Connection

- Algorithmic Heights

### Problems Used

- FIBO
- BINS
- INS
- MER
- MS
- QS
- PAR
- PAR3
- HEA
- HS
- INV
- MAJ
- 2SUM
- 3SUM
- MED
- PS

### Concepts

- Recurrence relations
- Binary search
- Sorting
- Merge sort
- Quick sort
- Partitioning
- Heaps
- Majority element
- Array scanning
- Inversions
- Selection problems

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| FIBO | Recurrence thinking for FIB, FIBD, CAT, MOTZ, and RNA-structure counting problems |
| BINS | Efficient lookup in sequence and k-mer tables |
| MER, MS, QS | Sorting biological strings, k-mers, suffix/indexing preparation |
| HEA, HS | Priority-queue thinking for graph and optimization problems |
| INV | Permutations and genome rearrangement intuition |
| 2SUM, 3SUM, MAJ | Efficient array-based reasoning for biological data processing |

### Suggested Treatment

| Problem | Role |
|---|---|
| FIBO | Fully explained |
| BINS | Fully explained |
| MER | Fully explained |
| MS | Fully explained |
| QS | Fully explained |
| INV | Worked example |
| HEA | Worked example |
| HS | Worked example |
| 2SUM | Worked example |
| 3SUM | Worked example |
| Remaining problems | Archive solution |

### Teaching Output

- Algorithmic foundations notebook
- Short lesson note
- Complexity comparison table

## Module 02: Algorithmic Foundations — Graph Algorithms

## Module 03: Biological Sequence Basics

## Module 04: Sequence Statistics, Motifs, and k-mers

## Module 05: Genetics and Probability

## Module 06: Dynamic Programming and Sequence Alignment

## Module 07: String Matching and Genome Indexing

## Module 08: Graphs and Genome Assembly

## Module 09: RNA Structure and Combinatorial Biology

## Module 10: Proteomics and Mass Spectrometry

## Module 11: Phylogenetics and Evolution

## Module 12: Practical Bioinformatics with Biopython

## Module 13: ML-ready Bioinformatics Bridge
