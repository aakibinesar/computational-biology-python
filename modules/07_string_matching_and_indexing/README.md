# Module 07: String Matching and Genome Indexing

## Purpose

This module focuses on string-matching algorithms and genome-indexing techniques used in computational biology.

Biological sequences such as DNA, RNA, and proteins can be represented as strings. Because of this, many bioinformatics problems depend on efficient methods for finding patterns, matching motifs, building indexes, and searching large sequence collections.

This module connects simple Rosalind motif-search problems with more advanced string algorithms such as KMP, tries, suffix structures, and Burrows-Wheeler-based indexing.

## Core Concepts

- Exact pattern matching
- Prefix functions and failure arrays
- Trie construction
- Suffix trees and suffix arrays
- Repeated substring discovery
- Genome-scale indexing
- Burrows-Wheeler Transform
- Approximate pattern matching
- Classical supplementary string-matching algorithms

## Rosalind Problems Covered

| Problem ID | Topic | Treatment |
|---|---|---|
| SUBS | Finding a motif in DNA | Cross-module reference |
| KMP | Failure array / prefix-based string matching | Fully explained |
| TRIE | Trie construction | Fully explained |
| SUFF | Suffix tree / suffix representation | Worked example |
| LING | Linguistic complexity | Worked example |
| MREP | Maximal repeats | Worked example |
| LREP | Longest repeated substring | Archive solution |
| BA1A–BA1N | Pattern matching, k-mers, approximate matching | Cross-module reference |
| BA9A–BA9R | Suffix arrays, BWT, and genome indexing | Archive / selected worked examples |

## Supplementary Algorithms

This module also includes supplementary implementations of classical string-matching algorithms:

| Algorithm | File | Relevance |
|---|---|---|
| Boyer-Moore | `supplementary_algorithms/boyer_moore.py` | Efficient exact pattern matching using character-shift heuristics |
| Z-algorithm | `supplementary_algorithms/z_algorithm.py` | Prefix-based preprocessing for fast pattern matching |

These are not direct Rosalind problem solutions. They are included to strengthen the connection between Rosalind string problems and general-purpose string algorithms used in computational biology.

## Learning Outcomes

After completing this module, a learner should be able to:

- explain why biological sequence analysis can be treated as a string-processing problem;
- implement exact pattern matching for DNA-style sequences;
- understand how prefix-based algorithms support faster pattern search;
- represent sets of patterns using tries;
- understand how suffix-based structures support large-scale sequence indexing;
- connect classical string algorithms to genome-search and motif-discovery tasks;
- distinguish between direct Rosalind solutions and supplementary algorithmic material.

## Connection to Later Modules

This module supports later work in genome assembly, sequence-feature extraction, and ML-ready bioinformatics workflows.

String matching connects directly to:

- Module 04: Sequence Statistics, Motifs, and k-mers
- Module 08: Graphs and Genome Assembly
- Module 13: ML-ready Bioinformatics Bridge

The concepts here also support practical tasks such as motif search, read mapping foundations, sequence indexing, k-mer feature extraction, and genome-scale pattern matching.
