# Lesson Plans

This file converts the original **Bioinformatics Workshop Fiesta 2020/21: Introduction to Python** structure into reusable lesson plans for the current repository.

The original workshop had 8 sessions. Each session was approximately 4 hours and followed a two-part structure:

```text
Session A: lecture explanation, concepts, and guided code examples
Session B: hands-on coding, live demonstration, Rosalind practice, and reflection
```

These lesson plans are public-facing, cleaned, and modernized for the repository. They should not be treated as exact copies of the original workshop delivery.

## Lesson Plan Overview

| Session | Original Topic | Current Teaching Focus | Main Repository Links |
|---:|---|---|---|
| 1 | The concept of programming language | programming concepts, Python motivation, setup, Rosalind introduction | Module 00, Notebook 01 |
| 2 | Introduction, variable and expressions | variables, expressions, debugging, strings, arithmetic | Module 00, Notebook 01, Exercise 01–02 |
| 3 | Flow control | conditionals, functions, lists, string/list logic | Module 00, Notebook 01, Exercise 03 |
| 4 | Repetition | loops, list comprehension, dictionaries, tuples | Module 00, Notebook 01, Notebook 02 |
| 5 | Input/Output | reading/writing files, FASTA, FASTQ | Notebook 01, Notebook 06 |
| 6 | Method, Biopython | functions/methods and introductory Biopython | Notebook 06, Exercise 05 |
| 7 | Biopython I | Seq, SeqIO, FASTA/GenBank records, Rosalind Armory | Notebook 06, Exercise 05–06 |
| 8 | Biopython II | Entrez, translation, FASTQ, alignment workflows, wrap-up | Notebook 06, Exercise 06 |

---

# Session 1: Programming Concepts and Workshop Orientation

## Original Topic

The concept of programming language.

## Learning Goals

By the end of this session, learners should be able to:

- explain the major building blocks of a programming language;
- understand why Python is useful for beginners and bioinformatics learners;
- recognize variables, control structures, data structures, syntax, and tools;
- create or access a Rosalind account;
- understand the workshop learning model.

## Key Concepts

- programming languages as structured systems;
- variables;
- control structures;
- data structures;
- syntax;
- tools and IDEs;
- Python readability;
- Rosalind as a problem-solving platform.

## Session A: Conceptual Lecture

Suggested flow:

1. Introduce the workshop and learning pathway.
2. Explain why programming languages share common building blocks.
3. Discuss the five core concepts:
   - variables;
   - control structures;
   - data structures;
   - syntax;
   - tools.
4. Explain why Python is suitable for beginner bioinformatics teaching.
5. Introduce Rosalind.

## Session B: Hands-on Practice

Suggested activities:

1. Install or open Python.
2. Open a Python shell or notebook.
3. Run a first command.
4. Create a Rosalind account.
5. Solve or inspect `INI1`.

## Related Repository Files

```text
notebooks/01_python_for_bioinformatics.ipynb
modules/00_python_for_bioinformatics/
teaching/exercises/01_python_variables_and_arithmetic.md
```

## Reflection Prompt

What is one programming concept that seems similar to something you already know from biology, mathematics, or data analysis?

---

# Session 2: Variables, Expressions, Strings, and Arithmetic

## Original Topic

Introduction, variable and expressions.

## Learning Goals

By the end of this session, learners should be able to:

- assign values to variables;
- distinguish strings, integers, floats, and booleans;
- use arithmetic operators;
- understand syntax errors and traceback errors;
- use string indexing and slicing;
- connect string operations to DNA sequence tasks.

## Key Concepts

- variables;
- expressions;
- statements;
- debugging;
- print function;
- comments;
- type conversion;
- string indexing;
- string slicing;
- string methods.

## Session A: Conceptual Lecture

Suggested flow:

1. Explain sequential execution.
2. Introduce debugging:
   - syntax errors;
   - logic errors;
   - semantic errors.
3. Demonstrate `print()`.
4. Explain variable assignment and naming.
5. Show arithmetic operators.
6. Introduce strings, indexing, and slicing.

## Session B: Hands-on Practice

Suggested Rosalind progression:

```text
INI2 → DNA
INI3 → RNA
```

Teaching pattern:

```text
basic Python task
→ biological sequence version
```

## Suggested Exercise Files

```text
teaching/exercises/01_python_variables_and_arithmetic.md
teaching/exercises/02_strings_and_dna.md
```

## Related Repository Files

```text
notebooks/01_python_for_bioinformatics.ipynb
notebooks/03_sequence_statistics_motifs_kmers.ipynb
modules/03_biological_sequence_basics/
```

## Reflection Prompt

Why are strings especially important in computational biology?

---

# Session 3: Flow Control, Functions, and Lists

## Original Topic

Flow control.

## Learning Goals

By the end of this session, learners should be able to:

- write `if`, `else`, and `elif` statements;
- use comparison operators;
- define simple functions;
- call functions with parameters;
- understand return values;
- understand variable scope;
- create and manipulate lists;
- connect list and string operations to sequence analysis.

## Key Concepts

- boolean expressions;
- comparison operators;
- conditional execution;
- functions;
- parameters;
- return values;
- default parameters;
- scope;
- lists;
- indexing and slicing lists;
- list methods.

## Session A: Conceptual Lecture

Suggested flow:

1. Introduce conditionals with simple examples.
2. Explain boolean expressions.
3. Demonstrate `if`, `else`, and `elif`.
4. Introduce functions as reusable code.
5. Explain function parameters and return values.
6. Introduce lists and list operations.

## Session B: Hands-on Practice

Suggested activities:

1. Write a conditional statement.
2. Write a simple function.
3. Process a list of values.
4. Connect loops/conditions to a DNA task.

Suggested Rosalind connection:

```text
INI4 → REVC
```

## Suggested Exercise File

```text
teaching/exercises/03_conditions_loops_reverse_complement.md
```

## Related Repository Files

```text
notebooks/01_python_for_bioinformatics.ipynb
modules/00_python_for_bioinformatics/
modules/03_biological_sequence_basics/
```

## Reflection Prompt

Why are functions useful when solving multiple biological sequence problems?

---

# Session 4: Repetition, Dictionaries, Tuples, and Sequence Counting

## Original Topic

Repetition.

## Learning Goals

By the end of this session, learners should be able to:

- write `while` loops;
- write `for` loops;
- use `range()`;
- loop through strings and lists;
- use list comprehensions;
- use dictionaries for counting;
- understand tuples and dictionary items;
- connect dictionaries to nucleotide, codon, and k-mer counting.

## Key Concepts

- while loops;
- for loops;
- break and continue;
- range;
- string iteration;
- list iteration;
- list comprehension;
- dictionaries;
- key-value pairs;
- tuples;
- sorting dictionary items.

## Session A: Conceptual Lecture

Suggested flow:

1. Explain repetition as a core strength of programming.
2. Compare `while` and `for` loops.
3. Demonstrate looping over numbers.
4. Demonstrate looping over strings.
5. Introduce list comprehensions.
6. Introduce dictionaries for counting.
7. Explain tuples and dictionary `.items()`.

## Session B: Hands-on Practice

Suggested activities:

1. Count letters in a string.
2. Count DNA nucleotides using a dictionary.
3. Write a motif-search loop.
4. Introduce recurrence through Fibonacci-style looping.

Suggested Rosalind connections:

```text
FIB
HAMM
SUBS
FIBD
```

## Suggested Exercise File

```text
teaching/exercises/04_recurrence_and_sequence_comparison.md
```

## Related Repository Files

```text
notebooks/02_algorithmic_foundations.ipynb
notebooks/03_sequence_statistics_motifs_kmers.ipynb
notebooks/04_dynamic_programming_alignment.ipynb
```

## Reflection Prompt

Why are dictionaries a natural structure for biological counting tasks?

---

# Session 5: Input/Output, FASTA, and FASTQ

## Original Topic

Input/Output.

## Learning Goals

By the end of this session, learners should be able to:

- read keyboard input;
- open and read files;
- write output files;
- understand file handles;
- explain why large files should be processed carefully;
- recognize FASTA format;
- recognize FASTQ format;
- understand why biological data often arrives in structured text files.

## Key Concepts

- `input()`;
- `open()`;
- read mode;
- write mode;
- append mode;
- file handles;
- line-by-line reading;
- closing files;
- FASTA;
- FASTQ;
- sequence identifiers;
- quality scores.

## Session A: Conceptual Lecture

Suggested flow:

1. Review output with `print()`.
2. Introduce keyboard input.
3. Explain opening, reading, writing, and appending files.
4. Discuss line-by-line file processing.
5. Introduce FASTA format.
6. Introduce FASTQ format.

## Session B: Hands-on Practice

Suggested activities:

1. Read a small text file.
2. Count lines in a file.
3. Parse a simple FASTA record manually.
4. Explain the four-line structure of FASTQ.

## Related Repository Files

```text
notebooks/01_python_for_bioinformatics.ipynb
notebooks/06_biopython_ml_ready_features.ipynb
modules/12_practical_bioinformatics_biopython/
```

## Reflection Prompt

Why are FASTA and FASTQ foundational file formats in computational biology?

---

# Session 6: Methods, Functions, and Introduction to Biopython

## Original Topic

Method, Biopython.

## Learning Goals

By the end of this session, learners should be able to:

- distinguish functions and methods;
- understand why libraries are useful;
- import Biopython;
- create a `Seq` object;
- compute complement and reverse complement using Biopython;
- connect plain Python sequence logic to library-supported workflows.

## Key Concepts

- functions;
- methods;
- libraries;
- imports;
- Biopython;
- `Bio.Seq`;
- `Seq` objects;
- complement;
- reverse complement.

## Session A: Conceptual Lecture

Suggested flow:

1. Review user-defined functions.
2. Explain methods as functions attached to objects.
3. Introduce libraries and imports.
4. Explain Biopython as a bioinformatics library.
5. Demonstrate `Seq` objects.

## Session B: Hands-on Practice

Suggested activities:

1. Create a `Seq` object.
2. Compute complement and reverse complement.
3. Compare plain Python and Biopython approaches.
4. Connect to Rosalind Armory `INI`.

## Suggested Exercise File

```text
teaching/exercises/05_biopython_intro.md
```

## Related Repository Files

```text
notebooks/06_biopython_ml_ready_features.ipynb
modules/12_practical_bioinformatics_biopython/
```

## Reflection Prompt

When is it better to use a library instead of writing everything manually?

---

# Session 7: Biopython I — FASTA, SeqIO, and GenBank Records

## Original Topic

Biopython I.

## Learning Goals

By the end of this session, learners should be able to:

- parse FASTA records using `SeqIO`;
- inspect sequence IDs and descriptions;
- understand `SeqRecord` objects;
- select records based on length;
- understand GenBank-style records;
- connect Biopython parsing to Rosalind Armory tasks.

## Key Concepts

- `Bio.SeqIO`;
- FASTA parsing;
- `SeqRecord`;
- record ID;
- record name;
- description;
- annotations;
- GenBank;
- shortest-sequence selection.

## Session A: Conceptual Lecture

Suggested flow:

1. Review FASTA format.
2. Introduce `SeqIO.parse()`.
3. Explain sequence records.
4. Show record fields:
   - ID;
   - name;
   - description;
   - sequence;
   - annotations.
5. Introduce GenBank records conceptually.

## Session B: Hands-on Practice

Suggested Rosalind connections:

```text
FRMT
GBK
```

Suggested activities:

1. Parse multiple FASTA records.
2. Print each record ID and sequence length.
3. Find the shortest sequence.
4. Discuss Entrez/GenBank retrieval carefully.

## Suggested Exercise Files

```text
teaching/exercises/05_biopython_intro.md
teaching/exercises/06_biopython_armory.md
```

## Related Repository Files

```text
notebooks/06_biopython_ml_ready_features.ipynb
modules/12_practical_bioinformatics_biopython/
```

## Reflection Prompt

What extra information does a `SeqRecord` contain beyond the sequence itself?

---

# Session 8: Biopython II — Entrez, Translation, FASTQ, and Alignment

## Original Topic

Biopython II.

## Learning Goals

By the end of this session, learners should be able to:

- describe Entrez search and fetch workflows;
- explain why biological database queries need care;
- translate DNA to protein;
- understand genetic code table selection;
- parse FASTQ records;
- convert FASTQ-style data to FASTA-style output;
- understand pairwise global alignment workflows;
- connect Biopython practice to future ML-ready sequence analysis.

## Key Concepts

- `Bio.Entrez`;
- NCBI search;
- GenBank retrieval;
- translation;
- genetic code tables;
- FASTQ parsing;
- quality scores;
- FASTQ to FASTA conversion;
- pairwise alignment;
- workflow interpretation.

## Session A: Conceptual Lecture

Suggested flow:

1. Review Biopython sequence records.
2. Introduce Entrez search/fetch idea.
3. Discuss responsible database access.
4. Demonstrate DNA translation.
5. Explain FASTQ quality scores.
6. Introduce pairwise alignment conceptually.

## Session B: Hands-on Practice

Suggested Rosalind connections:

```text
GBK
PTRA
TFSQ
NEED
```

Suggested activities:

1. Translate a DNA sequence.
2. Convert FASTQ records to FASTA-style output.
3. Describe an Entrez query workflow.
4. Interpret what a global alignment does.
5. Wrap up the workshop and discuss independent learning.

## Suggested Exercise File

```text
teaching/exercises/06_biopython_armory.md
```

## Related Repository Files

```text
notebooks/06_biopython_ml_ready_features.ipynb
mini_projects/ml_ready_sequence_features/
modules/13_ml_ready_bioinformatics_bridge/
```

## Reflection Prompt

How can Biopython workflows become the first step toward ML-ready biological datasets?

---

# Suggested Assessment and Reflection Structure

The original workshop used reflection forms and coding tasks. A public-facing version can use:

| Assessment Type | Purpose |
|---|---|
| quick reflection questions | check conceptual understanding |
| small coding tasks | reinforce Python syntax |
| Rosalind problems | connect programming to biological data |
| mini-project outputs | show applied workflow understanding |
| final reflection | encourage independent learning |

## Suggested Final Learner Task

Build a small feature table from DNA sequences with:

- sequence ID;
- length;
- GC content;
- AT content;
- nucleotide counts;
- k-mer counts.

This connects the workshop material to:

```text
mini_projects/ml_ready_sequence_features/
```

---

# Notes for Future Improvement

Future versions may add:

- timing breakdowns for each session;
- instructor notes;
- solution keys;
- slide references;
- recorded-demo notes;
- additional Biopython exercises;
- a beginner-to-intermediate assessment rubric.
