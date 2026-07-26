"""
Run feature extraction for the ML-ready sequence features mini-project.
"""

from pathlib import Path

from sequence_features import build_feature_table, load_fasta_file, save_feature_table


def main() -> None:
    project_dir = Path(__file__).resolve().parent

    input_path = project_dir / "example_sequences.fasta"
    output_path = project_dir / "outputs" / "sequence_features.csv"

    records = load_fasta_file(input_path)

    feature_table = build_feature_table(
        records,
        k=2,
        normalize_kmers=True,
        include_canonical_kmers=False,
    )

    save_feature_table(feature_table, output_path)

    print("Feature extraction complete.")
    print(f"Input records: {len(records)}")
    print(f"Output file: {output_path}")
    print()
    print(feature_table)


if __name__ == "__main__":
    main()
