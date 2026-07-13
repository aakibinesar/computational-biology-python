"""
Boyer-Moore string matching using the bad-character heuristic.

This implementation is included as supplementary material for
Module 07: String Matching and Genome Indexing.

The function returns zero-based Python indices. For Rosalind-style
one-based positions, add 1 to each returned index.
"""


def build_bad_character_table(pattern: str) -> dict[str, int]:
    """
    Build the bad-character table for the Boyer-Moore algorithm.

    The table stores the rightmost position of each character in the pattern.

    Args:
        pattern: Pattern string.

    Returns:
        A dictionary mapping each character to its rightmost index.
    """
    return {character: index for index, character in enumerate(pattern)}


def boyer_moore_search(
    text: str,
    pattern: str,
    case_sensitive: bool = True,
) -> list[int]:
    """
    Find all occurrences of a pattern in a text using Boyer-Moore search.

    This implementation uses the bad-character heuristic, which compares
    the pattern from right to left and shifts the pattern when a mismatch
    is found.

    Args:
        text: Text to search within.
        pattern: Pattern to search for.
        case_sensitive: Whether matching should be case-sensitive.

    Returns:
        A list of zero-based starting positions where the pattern occurs.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    if not case_sensitive:
        text = text.lower()
        pattern = pattern.lower()

    text_length = len(text)
    pattern_length = len(pattern)
    bad_character = build_bad_character_table(pattern)

    matches = []
    shift = 0

    while shift <= text_length - pattern_length:
        pattern_index = pattern_length - 1

        while (
            pattern_index >= 0
            and pattern[pattern_index] == text[shift + pattern_index]
        ):
            pattern_index -= 1

        if pattern_index < 0:
            matches.append(shift)

            next_index = shift + pattern_length

            if next_index < text_length:
                next_character = text[next_index]
                shift += pattern_length - bad_character.get(next_character, -1)
            else:
                shift += 1

        else:
            mismatched_character = text[shift + pattern_index]
            rightmost_position = bad_character.get(mismatched_character, -1)
            shift += max(1, pattern_index - rightmost_position)

    return matches


def to_rosalind_positions(indices: list[int]) -> list[int]:
    """
    Convert zero-based Python indices to one-based Rosalind-style positions.
    """
    return [index + 1 for index in indices]


if __name__ == "__main__":
    sample_text = "ACGTACGTGACG"
    sample_pattern = "ACG"

    zero_based_matches = boyer_moore_search(sample_text, sample_pattern)
    one_based_matches = to_rosalind_positions(zero_based_matches)

    print("Zero-based matches:", zero_based_matches)
    print("Rosalind-style one-based matches:", one_based_matches)
