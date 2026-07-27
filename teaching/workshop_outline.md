# Workshop Outline

## Bioinformatics Workshop Fiesta 2020/21: Introduction to Python

This file summarizes the structure of the original **Introduction to Python** workshop and explains how it is adapted into the current computational biology curriculum.

## Workshop Summary

| Item | Details |
|---|---|
| Workshop title | Introduction to Python |
| Workshop series | Bioinformatics Workshop Fiesta 2020/21 |
| Format | Online |
| Number of sessions | 8 sessions |
| Schedule | Saturdays, 13:00–17:00 GMT+8 |
| Dates | 31 October 2020 – 19 December 2020 |
| Platforms | Zoom, Moodle, Telegram |
| Teaching format | Lecture explanation, live coding, Rosalind home tasks, reflection activities |
| Core tools | Python, Rosalind, Biopython |

## Original 8-Session Structure

| Session | Date | Original Topic | Repository Connection |
|---|---:|---|---|
| 1 | 31 Oct 2020 | The concept of programming language | Python foundations, variables, syntax, tools |
| 2 | 7 Nov 2020 | Introduction, variable and expressions | variables, expressions, debugging, strings |
| 3 | 14 Nov 2020 | Flow control | conditionals, functions, lists |
| 4 | 21 Nov 2020 | Repetition | loops, list comprehension, dictionaries, tuples |
| 5 | 28 Nov 2020 | Input/Output | file handling, FASTA, FASTQ |
| 6 | 5 Dec 2020 | Method, Biopython | functions/methods, beginning Biopython |
| 7 | 12 Dec 2020 | Biopython I | Seq, SeqIO, FASTA/GenBank parsing, Rosalind Armory |
| 8 | 19 Dec 2020 | Biopython II | Entrez, translation, sequence utilities, FASTQ, alignment/tool workflows |

## Teaching Model

The workshop followed a two-part teaching model.

### Session A: Conceptual Lecture

Session A focused on explaining the topic, walking through code snippets, introducing programming concepts, and connecting Python concepts to biological examples.

### Session B: Hands-on Practice

Session B focused on live coding, interactive debugging, solving selected Rosalind problems, small group or individual coding work, and weekly home tasks.

## Learning Progression

```text
Programming concepts
→ Python syntax and variables
→ strings and lists
→ conditionals and functions
→ loops, dictionaries, and tuples
→ input/output and biological file formats
→ Rosalind sequence problems
→ Biopython workflows
```

## Adaptation in This Repository

| Original Workshop Area | Repository Adaptation |
|---|---|
| Python basics | `notebooks/01_python_for_bioinformatics.ipynb` |
| variables, strings, lists, loops | Modules 00–04 |
| Rosalind problem solving | `original_rosalind_tracks/`, `solved_problem_index.md`, `rosalind_problem_sets.md` |
| FASTA/FASTQ | Notebook 01, Notebook 06, Module 12 |
| Biopython | Notebook 06 and `biopython_session_notes.md` |
| Applied sequence features | `mini_projects/ml_ready_sequence_features/` |

## What This Outline Does Not Claim

This outline does not claim that the original workshop covered the full scope of the current repository. The current repository extends beyond the workshop into algorithmic foundations, dynamic programming, genome assembly, and ML-ready feature construction.
