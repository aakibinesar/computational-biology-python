"""
Feature extraction utilities for ML-ready DNA sequence representation.

This file supports the mini-project:

mini_projects/ml_ready_sequence_features/

The functions are intentionally readable and teaching-oriented.
"""

from collections import Counter
from itertools import product
from pathlib import Path

import pandas as pd


VALID_DNA_BASES = {"A", "C", "G", "T"}


def clean_sequence(sequence: str) -> str:
    """
    Return an uppercase DNA sequence with whitespace removed.
    """
    return "".join(sequence.upper().split())


def validate_dna(sequence: str) -> bool:
    """
    Return True if a sequence contains only A, C, G, and T.
    """
    sequence = clean_sequence(sequence)
    return all(base in VALID_DNA_BASES for base in sequence)


def parse_fasta_text(text: str) -> dict[str, str]:
    """
    Parse FASTA-formatted text into a dictionary of record_id -> sequence.

    This simple parser is designed for teaching and small examples.
    """
    records = {}
    current_id = None
    current_sequence = []

    for line in text.strip().splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            if current_id is not None:
                records[current_id] = clean_sequence("".join(current_sequence))

            current_id = line[1:].strip()
            current_sequence = []
        else:
            current_sequence.append(line)

    if current_id is not None:
        records[current_id] = clean_sequence("".join(current_sequence))

    return records


def load_fasta_file(path: str | Path) -> dict[str, str]:
    """
    Load a FASTA file and return a dictionary of record_id -> sequence.
    """
    path = Path(path)
    return parse_fasta_text(path.read_text(encoding="utf-8"))


def gc_content(sequence: str) -> float:
    """
    Return GC content percentage for a DNA sequence.
    """
    sequence = clean_sequence(sequence)

    if not sequence:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100


def at_content(sequence: str) -> float:
    """
    Return AT content percentage for a DNA sequence.
    """
    sequence = clean_sequence(sequence)

    if not sequence:
        return 0.0

    at_count = sequence.count("A") + sequence.count("T")
    return (at_count / len(sequence)) * 100


def nucleotide_counts(sequence: str) -> dict[str, int]:
    """
    Return counts of A, C, G, and T in a DNA sequence.
    """
    sequence = clean_sequence(sequence)
    counts = Counter(sequence)

    return {
        "A": counts.get("A", 0),
        "C": counts.get("C", 0),
        "G": counts.get("G", 0),
        "T": counts.get("T", 0),
    }


def reverse_complement(sequence: str) -> str:
    """
    Return the reverse complement of a DNA sequence.
    """
    sequence = clean_sequence(sequence)
    complement = str.maketrans("ACGT", "TGCA")
    return sequence.translate(complement)[::-1]


def all_dna_kmers(k: int) -> list[str]:
    """
    Return all possible DNA k-mers in lexicographic order.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    return ["".join(kmer) for kmer in product("ACGT", repeat=k)]


def kmer_counts(sequence: str, k: int) -> dict[str, int]:
    """
    Return observed k-mer counts for a DNA sequence.
    """
    sequence = clean_sequence(sequence)

    if k <= 0:
        raise ValueError("k must be positive")

    if len(sequence) < k:
        return {}

    counts = Counter()

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        counts[kmer] += 1

    return dict(counts)


def kmer_frequencies(sequence: str, k: int) -> dict[str, float]:
    """
    Return normalized observed k-mer frequencies for a DNA sequence.
    """
    counts = kmer_counts(sequence, k)
    total = sum(counts.values())

    if total == 0:
        return {}

    return {
        kmer: count / total
        for kmer, count in counts.items()
    }


def canonical_kmer(kmer: str) -> str:
    """
    Return a reverse-complement-aware canonical version of a k-mer.

    The canonical k-mer is the lexicographically smaller of the k-mer
    and its reverse complement.
    """
    rc = reverse_complement(kmer)
    return min(kmer, rc)


def canonical_kmer_counts(sequence: str, k: int) -> dict[str, int]:
    """
    Return reverse-complement-aware k-mer counts.
    """
    raw_counts = kmer_counts(sequence, k)
    canonical_counts = Counter()

    for kmer, count in raw_counts.items():
        canonical_counts[canonical_kmer(kmer)] += count

    return dict(canonical_counts)


def build_feature_table(
    records: dict[str, str],
    k: int = 2,
    normalize_kmers: bool = True,
    include_canonical_kmers: bool = False,
) -> pd.DataFrame:
    """
    Build a feature table from DNA sequences.

    Args:
        records: Dictionary of record_id -> DNA sequence.
        k: k-mer size.
        normalize_kmers: If True, include k-mer frequencies.
                         If False, include raw k-mer counts.
        include_canonical_kmers: If True, use reverse-complement-aware k-mers.

    Returns:
        A pandas DataFrame where rows are sequences and columns are features.
    """
    vocabulary = all_dna_kmers(k)

    if include_canonical_kmers:
        vocabulary = sorted({canonical_kmer(kmer) for kmer in vocabulary})

    rows = []
    index = []

    for record_id, sequence in records.items():
        sequence = clean_sequence(sequence)

        if not validate_dna(sequence):
            raise ValueError(f"Invalid DNA sequence found in record: {record_id}")

        counts = nucleotide_counts(sequence)

        row = {
            "length": len(sequence),
            "gc_content": gc_content(sequence),
            "at_content": at_content(sequence),
            "count_A": counts["A"],
            "count_C": counts["C"],
            "count_G": counts["G"],
            "count_T": counts["T"],
        }

        if include_canonical_kmers:
            observed = canonical_kmer_counts(sequence, k)
        else:
            observed = kmer_counts(sequence, k)

        total_kmers = sum(observed.values())

        for kmer in vocabulary:
            value = observed.get(kmer, 0)

            if normalize_kmers:
                feature_name = f"kmer_freq_{kmer}"
                row[feature_name] = value / total_kmers if total_kmers else 0.0
            else:
                feature_name = f"kmer_count_{kmer}"
                row[feature_name] = value

        rows.append(row)
        index.append(record_id)

    return pd.DataFrame(rows, index=index)


def save_feature_table(feature_table: pd.DataFrame, output_path: str | Path) -> None:
    """
    Save a feature table as a CSV file.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    feature_table.to_csv(output_path)
