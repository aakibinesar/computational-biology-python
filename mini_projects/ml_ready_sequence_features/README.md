# ML-ready Sequence Features

This mini-project converts biological DNA sequences into a machine-learning-ready feature table.

It extends the notebook:

`notebooks/06_biopython_ml_ready_features.ipynb`

and supports:

- **Module 04: Sequence Statistics, Motifs, and k-mers**
- **Module 12: Practical Bioinformatics with Biopython**
- **Module 13: ML-ready Bioinformatics Bridge**

## Purpose

The goal is to show how biological sequences can be transformed into transparent numerical features before applying machine learning.

This project focuses on interpretable, beginner-friendly features:

- sequence length;
- GC content;
- AT content;
- nucleotide counts;
- k-mer counts;
- normalized k-mer frequencies;
- optional reverse-complement-aware features.

## Connection to Original Rosalind Solutions

This mini-project is connected to my original Rosalind solution archive, especially problems related to:

- DNA sequence counting;
- GC content;
- motifs;
- k-mers;
- FASTA parsing;
- sequence comparison;
- feature construction.

The code here is not a line-by-line copy of the original Rosalind solutions. It is a cleaned and reusable project version that builds on those concepts.

## Folder Structure

```text
ml_ready_sequence_features/
├── README.md
├── example_sequences.fasta
├── sequence_features.py
├── run_feature_extraction.py
└── outputs/
    └── .gitkeep
```

## How to Run

From this folder:

```bash
python run_feature_extraction.py
```

This creates:

```text
outputs/sequence_features.csv
```

## Example Features

For each sequence, the feature table can include:

| Feature Type | Example |
|---|---|
| Basic length | `length` |
| Composition | `gc_content`, `at_content` |
| Nucleotide counts | `count_A`, `count_C`, `count_G`, `count_T` |
| k-mer counts | `kmer_count_AC`, `kmer_count_GT` |
| k-mer frequencies | `kmer_freq_AC`, `kmer_freq_GT` |

## Why This Matters

Many machine learning workflows require numerical input.

Biological sequences are strings, so they must first be represented as numerical features. k-mer based representations are a simple and widely used bridge between sequence analysis and machine learning.

## Important Note

This project demonstrates feature construction, not biological prediction.

Before using these features for real biological conclusions, a project would need:

- a larger dataset;
- clear biological labels;
- validation data;
- careful model evaluation;
- domain-specific interpretation.
