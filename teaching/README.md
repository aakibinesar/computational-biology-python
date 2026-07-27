# Teaching Materials

This folder contains teaching-oriented materials connected to the **Computational Biology with Python** curriculum.

The materials are based on prior workshop experience from **Bioinformatics Workshop Fiesta 2020/21: Introduction to Python**, where the instructor delivered an 8-session online workshop introducing Python, Biopython, and Rosalind-based bioinformatics problem solving.

The purpose of this folder is not to archive every original workshop file. Instead, it reorganizes the teaching approach into reusable, public-facing materials for learners and reviewers.

## Folder Index

| File or Folder | Purpose |
|---|---|
| `workshop_outline.md` | Summarizes the original 8-session workshop structure and how it maps to this repository |
| `rosalind_problem_sets.md` | Documents the curated Rosalind problem sequence used for teaching |
| `biopython_session_notes.md` | Summarizes the preserved Biopython/Armory teaching evidence and modernized repo direction |
| `feedback_summary.md` | Provides an anonymized summary of participant feedback and teaching reflections |
| `exercises/` | Placeholder for reusable learner exercises based on Python, Rosalind, and Biopython topics |
| `slides/` | Placeholder for notes about preserved lecture slide topics |

## Teaching Philosophy

The teaching approach follows a gradual progression:

```text
basic Python syntax
→ variables, strings, lists, loops, and dictionaries
→ file input/output
→ biological sequence problems
→ Rosalind-based practice
→ Biopython workflows
→ ML-ready biological sequence representation
```

The original workshop used a two-part structure:

```text
Session A: lecture explanation and code examples
Session B: hands-on coding, live demonstrations, and Rosalind problem solving
```

This repository extends that model into notebooks, modules, exercises, and mini-projects.

## Relationship to the Repository

| Repository Area | Teaching Connection |
|---|---|
| `notebooks/01_python_for_bioinformatics.ipynb` | Python basics applied to DNA strings |
| `notebooks/02_algorithmic_foundations.ipynb` | recurrence, search, sorting, and graph foundations |
| `notebooks/03_sequence_statistics_motifs_kmers.ipynb` | motifs, GC content, k-mers, and feature tables |
| `notebooks/06_biopython_ml_ready_features.ipynb` | Biopython, FASTA/FASTQ parsing, and ML-ready features |
| `mini_projects/ml_ready_sequence_features/` | applied feature extraction workflow |

## Modernization Note

The original workshop took place in 2020 and used the Python and Biopython teaching resources available at that time.

This repository updates those ideas using:

- Python 3;
- current Biopython conventions;
- Jupyter notebooks;
- reusable helper functions;
- cleaner project organization;
- privacy-conscious public documentation.

Older code patterns from the workshop, such as Python 2.7-era examples or deprecated Biopython modules, are treated as historical teaching evidence rather than copied directly.

## Privacy Note

Raw participant feedback files, identifiable response sheets, private appointment letters, and screenshots containing personal information should not be committed publicly.

Only anonymized summaries and public-facing teaching materials should be included in this repository.
