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

This block connects Python Village problems to the first layer of biological sequence analysis. The main goal is to show how basic Python syntax, string processing, dictionaries, loops, and file input/output become practical tools for DNA, RNA, and protein sequence problems.

### Core Dependency Chain

INI1–INI6 → DNA / RNA / REVC [I]  
INI1–INI6 → GC / SUBS / HAMM [I]  
INI3 / INI5 / INI6 → FASTA-style parsing problems such as GC / CONS / SPLC / FRMT / ORFR [I]  

DNA / RNA / REVC → PROT / ORF / SPLC / PTRA / ORFR [C]  
DNA / RNA / REVC → GC / SUBS / CONS / LCSM [C]  
PROT → PRTM / SPEC / BA4A [C]  
ORF / SPLC → practical translation and protein inference workflows [C]  

### Implementation Dependencies

Python strings → DNA / RNA / REVC / SUBS [I]  
Python dictionaries → nucleotide counts, codon tables, k-mer counts, profile matrices [I]  
Python file reading → FASTA and FASTQ-style problems [I]  
Loops and conditionals → motif search, translation, ORF detection, sequence filtering [I]  
Lists and list indexing → consensus sequences, distance matrices, dynamic programming tables [I]  

### Teaching Interpretation

The learner first uses Python to manipulate ordinary strings and files. Those skills are then transferred to biological sequences. DNA, RNA, reverse complement, GC content, motif finding, and translation become the first examples of how general programming becomes computational biology.

### Problems Connected

- Python foundations: INI1, INI2, INI3, INI4, INI5, INI6
- Basic sequence analysis: DNA, RNA, REVC, GC, SUBS, HAMM
- Translation and ORF workflows: PROT, MRNA, ORF, SPLC, PTRA, ORFR
- Practical file-based workflows: FRMT, TFSQ, PHRE, FILT

## 2. Recurrence to Biological Counting

This block connects recurrence relations, combinatorics, and probability to biological counting problems. It shows how simple recurrence logic expands into population growth, RNA structure counting, Mendelian genetics, and probability-based biological modelling.

### Core Dependency Chain

FIBO → recurrence relations [C]  
FIBO → FIB / FIBD [C]  
FIB / FIBD → biological population recurrence models [C]  
FIB / FIBD → CAT / MOTZ / RNAS [C]  

INI1–INI6 → IPRB / IEV / LIA [I]  
Basic arithmetic and probability → IPRB / IEV / LIA [C]  
Combinatorial counting → ASPC / PPER / SSET / SETO / PERM / SIGN [C]  
Combinatorial counting → PMCH / MMCH / CAT / MOTZ [C]  

### Genetics and Probability Progression

IPRB → IEV → LIA [C]  
IPRB / IEV / LIA → AFRQ / SEXL / MEND [C]  
AFRQ / SEXL → WFMD / FOUN / EBIN [C]  
WFMD / FOUN → population-level allele-frequency modelling [C]  

### RNA Structure Counting Progression

RNA / REVC → PMCH / MMCH [C]  
PMCH / MMCH → CAT / MOTZ [C]  
CAT / MOTZ → RNAS [C]  
REVP / ITWV → motif and structural pattern reasoning [C]  

### Implementation Dependencies

Loops → recurrence computation [I]  
Lists and arrays → storing recurrence values [I]  
Functions → reusable recurrence formulas [I]  
Dictionaries and counters → combinatorial sequence counting [I]  
Probability formulas → inheritance and allele-frequency problems [C]  

### Teaching Interpretation

This block shows that recurrence and counting are not abstract exercises. They appear naturally in biological growth models, inheritance probability, genetic drift, and RNA structure enumeration. This is also a bridge between computer science algorithms and biological modelling.

### Problems Connected

- Recurrence foundations: FIBO, FIB, FIBD
- Genetics and probability: IPRB, IEV, LIA, AFRQ, MEND, SEXL, WFMD, FOUN, EBIN, INDC
- Combinatorics: ASPC, PPER, SSET, SETO, PERM, SIGN
- RNA counting and structure: PMCH, MMCH, CAT, MOTZ, RNAS

## 3. Strings to Motifs and Genome Indexing

This block connects basic string operations to motif finding, k-mer analysis, trie structures, suffix-based indexing, and genome-scale pattern matching. It shows how simple substring search develops into efficient string algorithms used in bioinformatics.

### Core Dependency Chain

DNA / RNA / REVC → SUBS [C]  
SUBS → KMP [C]  
SUBS → BA1A / BA1B / BA1D / BA1H [C]  
KMP → failure arrays and prefix-function reasoning [C]  
KMP → TRIE [C]  
TRIE → SUFF / BA9A / BA9D / BA9E [C]  
SUFF / BA9A / BA9D / BA9E → BA9I / BA9J / BA9M / BA9N [C]  

### Motif and k-mer Progression

GC → sequence composition features [C]  
SUBS → exact motif search [C]  
SUBS → BA1A / BA1D [C]  
BA1A / BA1B → frequent words and k-mer counting [C]  
BA1H → approximate pattern matching [C]  
CONS → profile matrices [C]  
CONS → BA2A–BA2H [C]  
LCSM → shared motif discovery [C]  
KMER → k-mer feature representation [C]  

### Genome Indexing Progression

SUBS → direct pattern matching [C]  
KMP → efficient exact pattern matching [C]  
TRIE → multiple-pattern representation [C]  
SUFF → suffix-based sequence representation [C]  
MREP / LREP / LING → repeated-substring and linguistic-complexity reasoning [C]  
BA9A–BA9R → suffix arrays, Burrows-Wheeler Transform, and genome-scale indexing [C]  

### Implementation Dependencies

Python strings → exact pattern matching [I]  
String slicing → k-mer generation and motif search [I]  
Dictionaries → k-mer frequency tables and profile matrices [I]  
Sorting → suffix arrays and lexicographic ordering [I]  
Graphs/trees → trie and suffix-tree representation [C]  

### Teaching Interpretation

This block shows a clear progression from simple motif search to genome-scale indexing. It connects beginner-friendly string processing with more advanced bioinformatics string algorithms such as KMP, tries, suffix structures, and Burrows-Wheeler-based pattern matching.

### Problems Connected

- Basic string search: SUBS
- Motif/statistics problems: GC, CONS, LCSM, KMER, PROB, EVAL, RSTR, CORR
- String algorithms: KMP, TRIE, SUFF, MREP, LREP, LING
- Textbook motif problems: BA1A–BA1N, BA2A–BA2H
- Genome indexing: BA9A–BA9R

## 4. Graph Algorithms to Genome Assembly

This block connects graph-theoretic problems from Algorithmic Heights to genome assembly problems from Bioinformatics Stronghold and the Textbook Track. It shows how abstract graph algorithms become practical tools for sequence reconstruction.

### Core Dependency Chain

DEG / DDEG → graph representation [I]  
BFS / CC → graph traversal and connectivity [C]  
DAG / TS → directed graph ordering [C]  
DIJ / BF / SDAG → weighted path reasoning [C]  
SCC / SC → strongly connected directed graph reasoning [C]  

DEG / DDEG / BFS / CC → GRPH / TREE [C]  
GRPH → LONG [C]  
KMER / BA3A → DBRU / BA3D / BA3E [C]  
DBRU / BA3D / BA3E → PCOV / GASM / GREP [C]  
BA3D / BA3E → BA3F / BA3G / BA3H [C]  
BA3F / BA3G / BA3H → genome reconstruction from Eulerian paths/cycles [C]  

### Genome Assembly Progression

KMER → k-mer generation [C]  
KMER → BA3A / BA3B / BA3C [C]  
BA3A / BA3B / BA3C → graph construction from strings and k-mers [C]  
BA3D / BA3E → de Bruijn graph construction [C]  
BA3F / BA3G → Eulerian cycle and Eulerian path reasoning [C]  
BA3H → genome reconstruction from a path [C]  
DBRU → de Bruijn graph construction from reads [C]  
PCOV → perfect-coverage genome reconstruction [C]  
GASM → genome assembly using graph structure [C]  
GREP → alternative paths in assembly graphs [C]  
ASMQ → assembly quality measurement [C]  

### Implementation Dependencies

Dictionaries → adjacency lists [I]  
Lists of tuples/strings → graph edges and k-mers [I]  
Sets → unique nodes and edges [I]  
Queues/stacks → BFS and graph traversal [I]  
Directed graph representation → de Bruijn graphs and assembly graphs [I]  

### Teaching Interpretation

This block is one of the strongest CS-to-bioinformatics bridges. It demonstrates that genome assembly can be taught as a graph problem. General graph ideas such as nodes, edges, degrees, paths, cycles, and connectivity become overlap graphs, de Bruijn graphs, Eulerian paths, and genome reconstruction workflows.

### Problems Connected

- Algorithmic graph foundations: DEG, DDEG, BFS, CC, BIP, DAG, DIJ, BF, CTE, TS, HDAG, NWC, SCC, 2SAT, GS, SC, SDAG, SQ
- Stronghold genome assembly: GRPH, TREE, LONG, DBRU, PCOV, GASM, GREP, ASMQ
- Textbook genome assembly: BA3A–BA3M

## 5. Dynamic Programming to Alignment

This block connects recurrence relations and dynamic programming to sequence comparison and alignment. It shows how simple recurrence thinking develops into longest common subsequence, edit distance, global alignment, local alignment, affine gaps, and graph-based alignment formulations.

### Core Dependency Chain

FIBO → recurrence relations [C]  
FIB / FIBD → biological recurrence models [C]  
FIBO / FIB → dynamic programming intuition [C]  

LCSQ → EDIT / EDTA [C]  
EDIT / EDTA → SCSP / CTEA [C]  
LCSQ / EDIT → GLOB / LOCA [C]  
GLOB / LOCA → GCON / GAFF / LAFF [C]  
GLOB / LOCA → OAP / SIMS / SMGB [C]  
BA5A–BA5D → BA5E–BA5N [C]  

### Sequence Comparison Progression

HAMM → basic pairwise sequence difference [C]  
LCSQ → subsequence-based similarity [C]  
EDIT → edit-distance-based similarity [C]  
EDTA → edit distance with alignment reconstruction [C]  
SCSP → combining related sequences [C]  
CTEA → counting optimal alignments [C]  

### Alignment Progression

GLOB → global alignment [C]  
GCON → global alignment with constant gap penalty [C]  
LOCA → local alignment [C]  
GAFF → global alignment with affine gap penalty [C]  
LAFF → local alignment with affine gap penalty [C]  
OAP → overlap alignment [C]  
SIMS → fitting motif-style alignment [C]  
SMGB → semiglobal alignment [C]  
OSYM / MGAP / MULT → advanced alignment extensions [C]  

### Textbook DP Progression

BA5A / BA5B → dynamic programming on grids and paths [C]  
BA5C → longest common subsequence [C]  
BA5D → longest path in a DAG [C]  
BA5E / BA5F → global and local alignment [C]  
BA5G → edit distance [C]  
BA5H / BA5I / BA5J → fitting, overlap, and affine-gap alignment [C]  
BA5L / BA5M / BA5N → alignment reconstruction and multiple-sequence concepts [C]  

### Implementation Dependencies

Nested loops → DP table filling [I]  
2D lists/matrices → alignment and edit-distance tables [I]  
Backtracking pointers → alignment reconstruction [I]  
Scoring matrices → global/local alignment [I]  
Graph/path reasoning → DP as path optimization [C]  

### Teaching Interpretation

This block shows dynamic programming as a central computational biology technique. It begins with recurrence and table-filling, then progresses to biological sequence similarity and alignment. This is one of the most important bridges between core CS algorithms and bioinformatics.

### Problems Connected

- Recurrence foundations: FIBO, FIB, FIBD
- Sequence comparison: HAMM, LCSQ, EDIT, EDTA, SCSP, CTEA
- Alignment: GLOB, GCON, LOCA, GAFF, LAFF, OAP, SIMS, SMGB, OSYM, MGAP, MULT
- Textbook dynamic programming/alignment: BA5A–BA5N

## 6. Sequence Features to ML-ready Representation

This block connects classical bioinformatics problems to machine-learning-ready biological sequence representation. It shows how features such as GC content, k-mer counts, motif presence, profile matrices, edit distance, and alignment scores can become structured inputs for downstream machine learning workflows.

### Core Dependency Chain

DNA / RNA / REVC → sequence cleaning and validation [I]  
GC → numerical sequence composition feature [C]  
KMER / BA1A / BA1B → k-mer frequency features [C]  
SUBS / LCSM / BA2A–BA2H → motif-based features [C]  
CONS → profile-matrix representation [C]  
HAMM / EDIT → distance-based similarity features [C]  
GLOB / LOCA / GAFF → alignment-score features [C]  
FRMT / TFSQ / PHRE / FILT → practical data preprocessing [I]  

GC / KMER / CONS / LCSM → feature matrix construction [C]  
HAMM / EDIT / GLOB / LOCA → similarity matrix construction [C]  
FRMT / TFSQ / PHRE / FILT → quality-controlled sequence input [I]  
Feature matrix → baseline classification or clustering [C]  

### Feature Engineering Progression

GC → single numerical feature [C]  
KMER → fixed-length feature vector [C]  
BA1A–BA1N → frequency, position, and approximate-match features [C]  
BA2A–BA2H → motif-discovery and profile-based features [C]  
CONS → profile matrix and consensus representation [C]  
LCSM → shared motif feature extraction [C]  
CORR → error-aware sequence cleaning [C]  

### Similarity-based Representation Progression

HAMM → pairwise distance feature [C]  
EDIT → edit-distance feature [C]  
LCSQ → subsequence-similarity feature [C]  
GLOB / LOCA → alignment-score feature [C]  
GAFF / LAFF → gap-aware biological similarity feature [C]  
Similarity features → clustering, nearest-neighbour style reasoning, or baseline classification [C]  

### Practical Workflow Progression

FRMT / GBK → sequence retrieval and record handling [I]  
TFSQ → FASTQ-to-FASTA conversion [I]  
PHRE / FILT / BPHR → quality-score filtering [I]  
ORFR → practical ORF detection [I]  
Biopython workflows → reusable input/output layer for real biological data [I]  

### ML Capstone Dependency Chain

FASTA/FASTQ input → sequence cleaning [I]  
Sequence cleaning → GC and k-mer extraction [I]  
GC and k-mer extraction → feature matrix [I]  
Feature matrix → baseline model or clustering method [C]  
Model output → interpretation of biological sequence features [C]  

### Implementation Dependencies

Python dictionaries → k-mer counting [I]  
NumPy arrays → numerical feature vectors [I]  
Pandas DataFrames → feature matrix construction [I]  
Scikit-learn workflow → train/test split, baseline model, evaluation [I]  
Matplotlib → simple visualization of sequence features or model outputs [I]  

### Teaching Interpretation

This block is the capstone of the portfolio. It shows how classical Rosalind-style bioinformatics problem solving can be converted into a modern ML-ready workflow. The goal is not to claim advanced AI research, but to demonstrate a clear bridge from algorithms and bioinformatics to computational biology, AI for health, and biological data science.

### Problems Connected

- Basic sequence features: DNA, RNA, REVC, GC
- Motifs and k-mers: SUBS, CONS, LCSM, KMER, BA1A–BA1N, BA2A–BA2H
- Distance and alignment features: HAMM, LCSQ, EDIT, GLOB, LOCA, GAFF
- Error and quality handling: CORR, FRMT, TFSQ, PHRE, FILT, BPHR
- Practical workflow: GBK, FRMT, TFSQ, PHRE, FILT, ORFR
