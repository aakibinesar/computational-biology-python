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

### Teaching Purpose

This module introduces graph algorithms as a foundation for genome assembly, phylogenetics, biological networks, and graph-based sequence analysis.

### Rosalind Track Connection

- Algorithmic Heights

### Problems Used

- DEG
- DDEG
- BFS
- CC
- BIP
- DAG
- DIJ
- BF
- CTE
- TS
- HDAG
- NWC
- SCC
- 2SAT
- GS
- SC
- SDAG
- SQ

### Concepts

- Graph representation
- Degree arrays
- Breadth-first search
- Connected components
- Bipartite graphs
- Directed acyclic graphs
- Topological sorting
- Shortest paths
- Negative cycles
- Strongly connected components
- 2-SAT and constraint modelling

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| DEG, DDEG | Graph representation for overlap graphs and de Bruijn graphs |
| BFS, CC | Assembly graph traversal and connectivity |
| BIP | Bipartite structures and biological network modelling |
| DAG, TS, HDAG | Ordered graph structures and dynamic programming on graphs |
| DIJ, BF, SDAG | Weighted paths, alignment graphs, and distance-based models |
| NWC | Negative cycle reasoning in weighted graph problems |
| SCC, SC | Strong connectivity in directed assembly graphs |
| 2SAT | Advanced constraint-based modelling |

### Connected Bioinformatics Problems

- GRPH
- TREE
- DBRU
- LONG
- PCOV
- GASM
- GREP
- ASMQ
- BA3A–BA3H
- NWCK
- NKEW
- CTBL
- CSTR

### Suggested Treatment

| Problem | Role |
|---|---|
| DEG | Worked example |
| DDEG | Worked example |
| BFS | Fully explained |
| CC | Fully explained |
| DAG | Fully explained |
| DIJ | Fully explained |
| SCC | Fully explained |
| 2SAT | Worked example |
| Remaining problems | Archive solution |

### Teaching Output

- Graph algorithms before genome assembly notebook
- Graph representation lesson note
- Exercise set connecting Algorithmic Heights graph problems to genome assembly and phylogenetics

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
