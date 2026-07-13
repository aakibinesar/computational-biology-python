# Supplementary String Matching Algorithms

This folder contains additional classical string-matching algorithms implemented in Python.

These files are not direct Rosalind problem solutions. They are included as supplementary algorithmic material for:

**Module 07: String Matching and Genome Indexing**

The purpose of this folder is to connect basic Rosalind-style motif search with more advanced string-matching methods used in sequence analysis and genome-scale pattern matching.

## Algorithms Included

| File | Algorithm | Purpose |
|---|---|---|
| `boyer_moore.py` | Boyer-Moore string matching | Efficient exact pattern matching using character-shift heuristics |
| `z_algorithm.py` | Z-algorithm | Prefix-based string preprocessing for fast pattern matching |

## Connection to Rosalind Problems

These algorithms complement problems such as:

- `SUBS` — finding a motif in DNA
- `KMP` — failure array and prefix-based matching
- `TRIE` — multiple-pattern representation
- `SUFF` — suffix-based sequence representation
- `BA1A–BA1N` — pattern matching and k-mer problems
- `BA9A–BA9R` — genome indexing and Burrows-Wheeler-style string processing

## Why These Algorithms Matter

Biological sequences are naturally represented as strings. Efficient string-matching algorithms are therefore important for:

- motif search,
- exact pattern matching,
- sequence preprocessing,
- genome indexing,
- read mapping foundations,
- and scalable biological sequence analysis.

## Notes

These implementations were migrated from an earlier standalone bioinformatics algorithms repository and reorganized here as part of the broader computational biology curriculum.
