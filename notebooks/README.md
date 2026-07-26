# Tutorial Notebooks

This folder contains tutorial-style Jupyter notebooks for the computational biology curriculum.

The notebooks turn selected Rosalind problems and module concepts into beginner-friendly, executable learning materials. They are teaching-oriented rewrites and explanations, not line-by-line copies of the original solution files.

The original solved Rosalind work is preserved under:

`original_rosalind_tracks/`

## Notebook Index

| Notebook | Related Modules | Focus | Status |
|---|---|---|---|
| [`01_python_for_bioinformatics.ipynb`](01_python_for_bioinformatics.ipynb) | Module 00 / Module 03 | Python basics, DNA strings, nucleotide counting, transcription, reverse complement, GC content, motif search, and FASTA parsing | Complete first version |
| [`02_algorithmic_foundations.ipynb`](02_algorithmic_foundations.ipynb) | Module 01 / Module 02 | Recurrence, binary search, sorting, merge sort, inversion counting, graph representation, BFS, and connected components | Complete first version |
| [`03_sequence_statistics_motifs_kmers.ipynb`](03_sequence_statistics_motifs_kmers.ipynb) | Module 04 / Module 13 | GC content, motifs, consensus sequences, profile matrices, shared motifs, k-mer counts, probability models, and feature tables | Complete first version |
| [`04_dynamic_programming_alignment.ipynb`](04_dynamic_programming_alignment.ipynb) | Module 06 / Module 13 | Recurrence, LCS, edit distance, alignment reconstruction, global alignment, local alignment, and distance matrices | Complete first version |
| [`05_graphs_genome_assembly.ipynb`](05_graphs_genome_assembly.ipynb) | Module 08 | k-mers, genome paths, overlap graphs, de Bruijn graphs, Eulerian paths, genome reconstruction, N50, and N75 | Complete first version |
| [`06_biopython_ml_ready_features.ipynb`](06_biopython_ml_ready_features.ipynb) | Module 12 / Module 13 | Biopython FASTA/FASTQ parsing, sequence records, GC features, ORF detection, quality filtering, k-mer features, feature matrices, and baseline clustering | Complete first version |

## Notebook Goals

The notebooks focus on:

- clear explanations;
- runnable Python examples;
- biological interpretation;
- reusable helper functions;
- links between algorithms and bioinformatics applications;
- preparation for ML-ready biological sequence analysis.

## Relationship to Original Rosalind Solutions

The notebooks are connected to the original solved Rosalind archive, but they are not intended to reproduce the old code exactly.

The repository uses this structure:

| Folder | Role |
|---|---|
| `original_rosalind_tracks/` | Preserves the original solved Rosalind work |
| `modules/` | Organizes problems into a teaching-oriented curriculum |
| `notebooks/` | Provides polished educational walkthroughs |
| `mini_projects/` | Extends selected concepts into applied workflows |

## Development Status

The first-pass notebook set is complete.

Future improvements may include:

- adding more biological examples;
- adding exercises with solutions;
- connecting selected notebook functions to module-level utility files;
- expanding the ML-ready sequence feature workflow into a full mini-project.
