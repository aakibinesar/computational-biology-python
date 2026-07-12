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

### Teaching Purpose

This module introduces the central biological sequence types used in computational biology: DNA, RNA, and protein sequences. It connects basic Python string processing to transcription, reverse complementation, translation, open reading frames, splicing, and simple sequence comparison.

### Rosalind Track Connection

- Bioinformatics Stronghold
- Bioinformatics Armory

### Problems Used

- DNA
- RNA
- REVC
- HAMM
- PROT
- MRNA
- ORF
- PRTM
- SPLC
- TRAN
- REVP
- SSEQ
- PTRA
- ORFR
- RVCO

### Concepts

- DNA sequence representation
- RNA transcription
- Reverse complement
- Hamming distance
- Codons and translation
- Open reading frames
- Protein mass
- RNA splicing
- Transition/transversion ratio
- Subsequence matching
- Reverse-palindromic restriction sites

### Prerequisite Foundations

- INI1–INI6
- Python strings
- Dictionaries
- File reading
- Basic loops and conditionals

### Connected Bioinformatics Applications

| Foundation Skill | Bioinformatics Connection |
|---|---|
| Python string processing | DNA, RNA, REVC, HAMM |
| Dictionary lookup | Codon tables for PROT, MRNA, ORF, PTRA |
| File parsing | FASTA-based sequence problems such as SPLC and ORFR |
| Substring/subsequence logic | SSEQ, REVP, motif and pattern problems |
| Biological sequence conversion | Transcription, translation, splicing, and ORF detection |

### Suggested Treatment

| Problem | Role |
|---|---|
| DNA | Fully explained |
| RNA | Fully explained |
| REVC | Fully explained |
| PROT | Fully explained |
| ORF | Fully explained |
| SPLC | Fully explained |
| HAMM | Worked example |
| MRNA | Worked example |
| PRTM | Worked example |
| TRAN | Worked example |
| REVP | Worked example |
| SSEQ | Worked example |
| PTRA | Worked example |
| ORFR | Worked example |
| RVCO | Archive solution |

### Teaching Output

- Biological sequence basics notebook
- Codon table teaching note
- DNA-to-protein workflow example
- Exercise set on transcription, translation, and ORF detection

## Module 04: Sequence Statistics, Motifs, and k-mers

### Teaching Purpose

This module moves from simple sequence manipulation to sequence-level statistics and feature extraction. It introduces GC content, motif finding, consensus sequences, k-mer counting, sequence probability, and motif discovery as foundations for both classical bioinformatics and machine-learning-ready biological sequence representation.

### Rosalind Track Connection

- Bioinformatics Stronghold
- Bioinformatics Textbook Track

### Problems Used

- GC
- SUBS
- CONS
- LCSM
- KMER
- PROB
- EVAL
- RSTR
- CORR
- BA1A–BA1N
- BA2A–BA2H

### Concepts

- GC content
- Motif search
- Consensus sequences
- Profile matrices
- Longest common substring
- k-mer counting
- Sequence probability
- Expected motif occurrence
- Error correction in reads
- Frequent words and approximate pattern matching
- Motif discovery
- Median string problem
- Profile-most probable k-mers

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 03: Biological Sequence Basics
- Python dictionaries
- String slicing
- Counting and frequency tables

### Connected Bioinformatics Applications

| Foundational Problem | Bioinformatics Connection |
|---|---|
| GC | Sequence composition and basic feature extraction |
| SUBS | Motif search and pattern matching |
| CONS | Profile matrices and consensus sequence construction |
| LCSM | Shared motif discovery across sequences |
| KMER | k-mer feature representation |
| PROB, EVAL, RSTR | Probability models for sequence patterns |
| BA1A–BA1N | Frequent words, reverse complements, approximate matching, and pattern positions |
| BA2A–BA2H | Motif discovery and profile-based sequence analysis |

### Connected ML-ready Applications

| Concept | ML Connection |
|---|---|
| GC content | Simple numerical sequence feature |
| k-mer counts | Feature vector construction |
| Motif presence/absence | Binary feature representation |
| Profile matrices | Probabilistic sequence representation |
| Approximate matching | Robust sequence similarity features |

### Suggested Treatment

| Problem | Role |
|---|---|
| GC | Fully explained |
| SUBS | Fully explained |
| CONS | Fully explained |
| LCSM | Fully explained |
| KMER | Fully explained |
| BA1A | Fully explained |
| BA1B | Fully explained |
| BA1H | Worked example |
| BA2A | Fully explained |
| BA2D | Worked example |
| PROB | Worked example |
| EVAL | Worked example |
| RSTR | Worked example |
| CORR | Worked example |
| Remaining BA1 and BA2 problems | Archive solution |

### Teaching Output

- Sequence statistics and motifs notebook
- k-mer feature extraction lesson note
- Motif discovery exercise set
- Bridge note connecting k-mers to ML-ready sequence features

## Module 05: Genetics and Probability

### Teaching Purpose

This module introduces probability, combinatorics, inheritance modelling, and population genetics through computational biology problems. It connects basic arithmetic, counting, and probability reasoning to Mendelian inheritance, allele frequencies, expected values, and genetic drift.

### Rosalind Track Connection

- Bioinformatics Stronghold

### Problems Used

- IPRB
- IEV
- LIA
- AFRQ
- MEND
- SEXL
- WFMD
- FOUN
- EBIN
- INDC
- ASPC
- PPER
- SSET
- SETO
- PERM
- SIGN

### Concepts

- Mendelian inheritance
- Dominant and recessive alleles
- Expected value
- Independent probability
- Binomial probability
- Allele frequency
- Wright-Fisher model
- Genetic drift
- Combinatorics
- Set operations
- Permutations and signed permutations

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Basic arithmetic
- Loops and conditionals
- Combinatorial counting
- Probability rules

### Connected Bioinformatics Applications

| Problem | Bioinformatics Connection |
|---|---|
| IPRB | Mendelian inheritance probability |
| IEV | Expected number of dominant phenotype offspring |
| LIA | Independent allele inheritance across generations |
| AFRQ | Allele frequency estimation |
| WFMD | Genetic drift using Wright-Fisher modelling |
| FOUN | Founder effect and allele frequency change |
| EBIN | Expected binomial outcomes |
| PERM, SIGN | Permutation-based reasoning used in genome rearrangement and combinatorics |

### Suggested Treatment

| Problem | Role |
|---|---|
| IPRB | Fully explained |
| IEV | Fully explained |
| LIA | Fully explained |
| WFMD | Fully explained |
| FOUN | Fully explained |
| AFRQ | Worked example |
| MEND | Worked example |
| SEXL | Worked example |
| EBIN | Worked example |
| INDC | Worked example |
| ASPC | Worked example |
| PPER | Archive solution |
| SSET | Archive solution |
| SETO | Archive solution |
| PERM | Worked example |
| SIGN | Worked example |

### Teaching Output

- Genetics and probability notebook
- Mendelian inheritance teaching note
- Probability model exercise set
- Short bridge note connecting classical probability to biological data modelling

## Module 06: Dynamic Programming and Sequence Alignment

## Module 07: String Matching and Genome Indexing

## Module 08: Graphs and Genome Assembly

## Module 09: RNA Structure and Combinatorial Biology

## Module 10: Proteomics and Mass Spectrometry

## Module 11: Phylogenetics and Evolution

## Module 12: Practical Bioinformatics with Biopython

## Module 13: ML-ready Bioinformatics Bridge
