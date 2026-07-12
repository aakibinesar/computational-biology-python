# Problem Dependency Map

This file maps prerequisite-style connections across the Rosalind-based curriculum. It combines:

- implementation prerequisites,
- conceptual prerequisites,
- and Rosalind-style progression logic where appropriate.

## Dependency Labels

- **[I] Implementation prerequisite** — coding skill required before solving the later problem.
- **[C] Conceptual prerequisite** — conceptually useful before moving to the later problem.
- **[R] Rosalind-style progression** — progression inspired by Rosalind's unlock/prerequisite structure, where applicable.

## High-level Dependency Flow

Python Village  
→ Algorithmic Heights  
→ Bioinformatics Stronghold  
→ Bioinformatics Textbook Track  
→ Bioinformatics Armory  
→ ML-ready Bioinformatics Bridge

## 1. Python to Sequence Analysis

INI1–INI6 → DNA / RNA / REVC / GC / SUBS [I]

## 2. Recurrence to Biological Counting

FIBO → FIB / FIBD [C]  
FIB / FIBD → CAT / MOTZ / RNAS [C]

## 3. Strings to Motifs and Genome Indexing

SUBS → KMP → TRIE → SUFF / BA9 problems [C]

## 4. Graph Algorithms to Genome Assembly

DEG / DDEG / BFS / CC / SCC → GRPH / DBRU / GASM / BA3 problems [C]

## 5. Dynamic Programming to Alignment

FIBO → LCSQ → EDIT → GLOB / LOCA / GAFF / BA5 problems [C]

## 6. Sequence Features to ML-ready Representation

GC / KMER / CONS / LCSM → k-mer features / motif features / feature matrix construction [C]
