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

### Teaching Purpose

This module introduces dynamic programming as one of the central algorithmic techniques in computational biology. It connects recurrence relations and sequence comparison problems to longest common subsequences, edit distance, shortest common supersequences, global alignment, local alignment, affine gap penalties, and alignment graph formulations.

### Rosalind Track Connection

- Algorithmic Heights
- Bioinformatics Stronghold
- Bioinformatics Textbook Track

### Problems Used

- FIBO
- FIB
- FIBD
- LCSQ
- EDIT
- EDTA
- SCSP
- CTEA
- GLOB
- GCON
- LOCA
- GAFF
- LAFF
- OAP
- SIMS
- SMGB
- OSYM
- MGAP
- MULT
- BA5A
- BA5B
- BA5C
- BA5D
- BA5E
- BA5F
- BA5G
- BA5H
- BA5I
- BA5J
- BA5K
- BA5L
- BA5M
- BA5N

### Concepts

- Recurrence relations
- Dynamic programming tables
- Longest common subsequence
- Edit distance
- Shortest common supersequence
- Counting optimal alignments
- Global sequence alignment
- Local sequence alignment
- Gap penalties
- Affine gap penalties
- Overlap alignment
- Fitting alignment
- Multiple sequence alignment
- Alignment as graph/path optimization

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 01: Algorithmic Foundations — Arrays, Sorting, and Searching
- Module 03: Biological Sequence Basics
- Recurrence relations
- Matrix/table construction
- String indexing and slicing

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| FIBO | Recurrence logic for biological growth and DP formulation |
| FIB, FIBD | Recurrence-based modelling with biological interpretation |
| LCSQ | Sequence similarity through longest common subsequence |
| EDIT, EDTA | Edit distance and alignment reconstruction |
| SCSP | Combining related sequences into a shortest common representation |
| CTEA | Counting optimal alignments |
| GLOB, GCON | Global alignment and gap-penalty models |
| LOCA | Local alignment and biologically meaningful subsequence matching |
| GAFF, LAFF | Affine gap penalties in realistic alignment models |
| OAP, SIMS, SMGB | Specialized alignment variants |
| BA5A–BA5N | Textbook-style dynamic programming and alignment formulations |

### Suggested Treatment

| Problem | Role |
|---|---|
| FIBO | Fully explained |
| FIB | Fully explained |
| LCSQ | Fully explained |
| EDIT | Fully explained |
| EDTA | Fully explained |
| SCSP | Worked example |
| GLOB | Fully explained |
| LOCA | Fully explained |
| GAFF | Fully explained |
| BA5C | Fully explained |
| BA5G | Fully explained |
| BA5L | Worked example |
| BA5M | Worked example |
| FIBD | Worked example |
| CTEA | Worked example |
| GCON | Worked example |
| LAFF | Worked example |
| OAP | Worked example |
| SIMS | Worked example |
| SMGB | Worked example |
| OSYM | Archive solution |
| MGAP | Archive solution |
| MULT | Archive solution |
| Remaining BA5 problems | Archive solution |

### Teaching Output

- Dynamic programming and sequence alignment notebook
- DP table visualization examples
- Sequence alignment lesson note
- Exercise set on LCS, edit distance, and global/local alignment
- Complexity comparison table for alignment algorithms

## Module 07: String Matching and Genome Indexing

### Teaching Purpose

This module connects basic motif search to efficient string-matching and indexing methods used in computational biology. It moves from direct substring search to prefix functions, tries, suffix-based structures, and Burrows-Wheeler-style indexing.

### Rosalind Track Connection

- Bioinformatics Stronghold
- Bioinformatics Textbook Track
- Related independent string-matching implementations

### Problems Used

- SUBS
- KMP
- TRIE
- SUFF
- LING
- MREP
- LREP
- BA1A
- BA1B
- BA1D
- BA1H
- BA9A
- BA9B
- BA9C
- BA9D
- BA9E
- BA9F
- BA9G
- BA9H
- BA9I
- BA9J
- BA9K
- BA9L
- BA9M
- BA9N
- BA9O
- BA9P
- BA9Q
- BA9R

### Concepts

- Exact pattern matching
- Approximate pattern matching
- Prefix functions
- Failure arrays
- Tries
- Suffix trees
- Suffix arrays
- Repeated substrings
- Genome indexing
- Burrows-Wheeler Transform
- Pattern matching at genome scale

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 01: Algorithmic Foundations — Arrays, Sorting, and Searching
- Module 04: Sequence Statistics, Motifs, and k-mers
- Python strings
- Dictionaries
- Sorting
- Prefix/suffix reasoning

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| SUBS | Direct motif search in DNA sequences |
| KMP | Efficient motif search using failure arrays |
| TRIE | Prefix-tree representation of biological patterns |
| SUFF | Suffix-based representation of whole sequences |
| MREP, LREP | Repeated sequence discovery |
| BA1A–BA1H | Frequent words, approximate matching, and pattern location |
| BA9A–BA9R | Genome indexing, suffix arrays, and Burrows-Wheeler-based search |

### Suggested Treatment

| Problem | Role |
|---|---|
| SUBS | Fully explained |
| KMP | Fully explained |
| TRIE | Fully explained |
| BA1A | Fully explained |
| BA1B | Fully explained |
| BA9A | Fully explained |
| BA9D | Fully explained |
| BA9E | Fully explained |
| SUFF | Worked example |
| MREP | Worked example |
| LING | Worked example |
| LREP | Archive solution |
| BA9I | Worked example |
| BA9J | Worked example |
| BA9M | Worked example |
| BA9N | Worked example |
| Remaining BA9 problems | Archive solution |

### Teaching Output

- String matching and genome indexing notebook
- Prefix-function and trie lesson note
- Suffix-array/suffix-tree overview
- Exercise set on motif search and genome-scale pattern matching

## Module 08: Graphs and Genome Assembly

### Teaching Purpose

This module connects graph algorithms to genome assembly. It shows how biological sequence reconstruction can be formulated using overlap graphs, de Bruijn graphs, paths, cycles, and graph traversal.

### Rosalind Track Connection

- Algorithmic Heights
- Bioinformatics Stronghold
- Bioinformatics Textbook Track

### Problems Used

- DEG
- DDEG
- BFS
- CC
- DAG
- SCC
- GRPH
- TREE
- LONG
- DBRU
- PCOV
- GASM
- GREP
- ASMQ
- BA3A
- BA3B
- BA3C
- BA3D
- BA3E
- BA3F
- BA3G
- BA3H
- BA3I
- BA3J
- BA3K
- BA3L
- BA3M

### Concepts

- Graph representation
- Overlap graphs
- de Bruijn graphs
- Genome reconstruction
- Eulerian paths
- Eulerian cycles
- Contigs
- Assembly quality
- Short-read assembly logic
- Graph connectivity
- Directed graph traversal

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 02: Algorithmic Foundations — Graph Algorithms
- Module 03: Biological Sequence Basics
- Module 04: Sequence Statistics, Motifs, and k-mers
- k-mer generation
- Graph construction
- Directed graph traversal

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| DEG, DDEG | Degree concepts for graph representation |
| BFS, CC | Connectivity and traversal of assembly graphs |
| DAG, SCC | Directed graph reasoning in assembly structures |
| GRPH | Overlap graph construction |
| TREE | Graph connectivity and missing edges |
| LONG | Genome reconstruction from overlaps |
| DBRU | de Bruijn graph construction from reads/k-mers |
| PCOV | Perfect coverage and cyclic reconstruction |
| GASM | Genome assembly using de Bruijn graphs |
| GREP | Alternative paths through assembly graphs |
| ASMQ | Assembly quality metrics |
| BA3A–BA3M | Textbook-style genome assembly graph problems |

### Suggested Treatment

| Problem | Role |
|---|---|
| GRPH | Fully explained |
| DBRU | Fully explained |
| BA3D | Fully explained |
| BA3E | Fully explained |
| BA3F | Fully explained |
| BA3H | Fully explained |
| GASM | Fully explained |
| TREE | Worked example |
| LONG | Worked example |
| PCOV | Worked example |
| GREP | Worked example |
| ASMQ | Worked example |
| BA3A | Worked example |
| BA3B | Worked example |
| BA3C | Worked example |
| Remaining BA3 problems | Archive solution |

### Teaching Output

- Graphs and genome assembly notebook
- de Bruijn graph lesson note
- Genome reconstruction exercise set
- Visual explanation of overlap graphs and de Bruijn graphs
- Short bridge note connecting graph algorithms to biological sequence assembly

## Module 09: RNA Structure and Combinatorial Biology

### Teaching Purpose

This module connects recurrence relations, combinatorics, matching, and dynamic programming to RNA structure-related problems. It shows how biological constraints such as base pairing can be represented computationally through counting, matching, and recursive decomposition.

### Rosalind Track Connection

- Bioinformatics Stronghold
- Algorithmic Heights

### Problems Used

- FIBO
- FIB
- FIBD
- PMCH
- MMCH
- CAT
- MOTZ
- RNAS
- REVP
- ITWV

### Concepts

- Recurrence relations
- RNA base pairing
- Perfect matchings
- Maximum matchings
- Catalan-style counting
- Motzkin-style counting
- Noncrossing matchings
- Recursive decomposition
- Reverse-palindromic sequences
- Interwoven motifs

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 01: Algorithmic Foundations — Arrays, Sorting, and Searching
- Module 03: Biological Sequence Basics
- Module 05: Genetics and Probability
- Module 06: Dynamic Programming and Sequence Alignment
- Recurrence relations
- Combinatorial counting
- RNA sequence handling

### Connected Bioinformatics Applications

| Foundation Problem | Bioinformatics Connection |
|---|---|
| FIBO | General recurrence thinking |
| FIB, FIBD | Biological recurrence models |
| PMCH | Perfect RNA base-pair matchings |
| MMCH | Maximum RNA base-pair matchings |
| CAT | Catalan-style noncrossing RNA matchings |
| MOTZ | Motzkin-style RNA secondary structure counting |
| RNAS | RNA secondary structure with wobble base pairs |
| REVP | Reverse-palindromic restriction sites |
| ITWV | Interwoven motif detection |

### Suggested Treatment

| Problem | Role |
|---|---|
| PMCH | Fully explained |
| MMCH | Worked example |
| CAT | Fully explained |
| MOTZ | Fully explained |
| RNAS | Fully explained |
| REVP | Worked example |
| ITWV | Worked example |
| FIB | Cross-module reference |
| FIBD | Cross-module reference |

### Teaching Output

- RNA structure and combinatorics lesson note
- Recurrence and matching explanation
- Worked examples on perfect and noncrossing matchings
- Exercise set on recursive counting in RNA structure problems
- Bridge note connecting RNA structure counting to dynamic programming

## Module 10: Proteomics and Mass Spectrometry

### Teaching Purpose

This module extends sequence analysis from nucleic acids to proteins and peptide sequencing. It introduces protein translation, amino acid mass, spectra, peptide reconstruction, spectral convolution, and mass-spectrometry-style computational problems.

### Rosalind Track Connection

- Bioinformatics Stronghold
- Bioinformatics Textbook Track

### Problems Used

- PROT
- PRTM
- SPEC
- CONV
- FULL
- PRSM
- SGRA
- PDPL
- BA4A
- BA4B
- BA4C
- BA4D
- BA4F
- BA4H
- BA4J
- BA4K

### Concepts

- Protein translation
- Amino acid mass tables
- Peptide mass calculation
- Prefix spectra
- Complete spectra
- Spectral convolution
- Peptide reconstruction
- Protein inference from spectra
- Spectrum graph reasoning
- Cyclopeptide sequencing
- Leaderboard peptide sequencing
- Peptide scoring

### Prerequisite Foundations

- Module 00: Python for Bioinformatics
- Module 03: Biological Sequence Basics
- Module 04: Sequence Statistics, Motifs, and k-mers
- Dictionary lookup
- Protein sequence representation
- Basic graph/path reasoning
- Numerical sequence processing

### Connected Bioinformatics Applications

| Problem | Bioinformatics Connection |
|---|---|
| PROT | Translation from RNA to protein |
| PRTM | Protein mass calculation |
| SPEC | Protein inference from prefix spectrum |
| CONV | Spectral convolution |
| FULL | Peptide reconstruction from complete spectrum |
| PRSM | Matching proteins against spectra |
| SGRA | Spectrum graph reconstruction |
| PDPL | Partial digest problem and distance-based reconstruction |
| BA4A | Translating RNA into peptide |
| BA4B | Finding DNA substrings encoding a peptide |
| BA4C | Cyclic spectrum generation |
| BA4D | Counting peptides by mass |
| BA4F | Cyclopeptide scoring |
| BA4H | Spectral convolution |
| BA4J | Linear spectrum generation |
| BA4K | Linear peptide scoring |

### Suggested Treatment

| Problem | Role |
|---|---|
| PROT | Cross-module reference |
| PRTM | Fully explained |
| SPEC | Fully explained |
| SGRA | Fully explained |
| BA4A | Fully explained |
| BA4B | Worked example |
| BA4C | Fully explained |
| BA4D | Worked example |
| BA4F | Worked example |
| BA4H | Worked example |
| BA4J | Worked example |
| BA4K | Worked example |
| CONV | Worked example |
| FULL | Worked example |
| PRSM | Worked example |
| PDPL | Archive solution |

### Teaching Output

- Proteomics and mass spectrometry notebook
- Amino acid mass table teaching note
- Peptide spectrum generation examples
- Exercise set on peptide mass and spectrum reconstruction
- Bridge note connecting graph/path reasoning to spectrum-based peptide inference

## Module 11: Phylogenetics and Evolution

## Module 12: Practical Bioinformatics with Biopython

## Module 13: ML-ready Bioinformatics Bridge
