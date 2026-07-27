# Teaching Materials

This folder contains teaching-oriented materials connected to the **Computational Biology with Python** curriculum.

The materials are based on prior workshop experience from **Bioinformatics Workshop Fiesta 2020/21: Introduction to Python**, an 8-session online workshop introducing Python, Biopython, and Rosalind-based bioinformatics problem solving.

The purpose of this folder is not to archive every original workshop file. Instead, it reorganizes the teaching approach into reusable, public-facing materials for learners, reviewers, and future teaching use.

## Folder Index

| File or Folder | Purpose |
|---|---|
| `workshop_outline.md` | Summarizes the original 8-session workshop structure and how it maps to this repository |
| `lesson_plans.md` | Converts the 8-session workshop into reusable lesson plans |
| `rosalind_problem_sets.md` | Documents the curated Rosalind problem sequence used for teaching |
| `biopython_session_notes.md` | Summarizes the preserved Biopython/Armory teaching material and modernized repo direction |
| `feedback_summary.md` | Provides an anonymized summary of participant feedback and teaching reflections |
| `exercises/` | Contains cleaned learner exercise sheets based on Python, Rosalind, and Biopython topics |
| `slides/` | Contains notes about preserved lecture slide topics and slide-to-notebook mapping |
| `workshop_record/` | Contains selected public-facing workshop record materials such as posters or redacted certificates |

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
Session A: lecture explanation and guided code examples
Session B: hands-on coding, live demonstrations, Rosalind problem solving, and reflection
```

This repository extends that model into notebooks, modules, exercises, lesson plans, and mini-projects.

## Relationship to the Repository

The teaching materials connect most directly to:

| Repository Area | Teaching Connection |
|---|---|
| `notebooks/01_python_for_bioinformatics.ipynb` | Python basics applied to DNA strings |
| `notebooks/02_algorithmic_foundations.ipynb` | recurrence, search, sorting, and graph foundations |
| `notebooks/03_sequence_statistics_motifs_kmers.ipynb` | motifs, GC content, k-mers, and feature tables |
| `notebooks/04_dynamic_programming_alignment.ipynb` | recurrence, edit distance, alignment, and sequence comparison |
| `notebooks/06_biopython_ml_ready_features.ipynb` | Biopython, FASTA/FASTQ parsing, and ML-ready features |
| `mini_projects/ml_ready_sequence_features/` | applied feature extraction workflow |

## Teaching Materials Created

| Material | Status |
|---|---|
| Workshop outline | Complete first version |
| Lesson plans | Complete first version |
| Rosalind problem-set summary | Complete first version |
| Biopython session notes | Complete first version |
| Feedback summary | Complete first version |
| Exercise sheets | Complete first version |
| Slide-topic README | Complete first version |
| Workshop record folder | Added separately by the repository owner |

## Original Workshop Scope

The original workshop focused on:

- Python programming foundations;
- selected Python Village problems;
- selected Bioinformatics Stronghold problems;
- selected Bioinformatics Armory problems;
- practical Biopython usage;
- live coding and weekly Rosalind home tasks.

The current repository extends that foundation into a broader computational biology curriculum, including algorithmic foundations, dynamic programming, genome assembly, and ML-ready sequence features.

## Modernization Note

The original workshop took place in 2020 and used the Python and Biopython teaching resources available at that time.

This repository updates those ideas using:

- Python 3;
- current Biopython conventions;
- Jupyter notebooks;
- reusable helper functions;
- cleaner project organization;
- privacy-conscious public documentation.

Older code patterns from the workshop, such as Python 2.7-era examples or deprecated Biopython modules, are treated as historical teaching material rather than copied directly.

## Privacy Note

Raw participant feedback files, identifiable response sheets, private appointment letters, and screenshots containing personal information should not be committed publicly.

Only anonymized summaries and public-facing teaching materials should be included in this repository.
