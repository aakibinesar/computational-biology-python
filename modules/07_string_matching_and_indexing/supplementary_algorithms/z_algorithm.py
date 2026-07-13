"""
Z-algorithm for string preprocessing and pattern matching.

This implementation is included as supplementary material for
Module 07: String Matching and Genome Indexing.

The Z-array stores, for each position i, the length of the longest substring
starting at i that also matches the prefix of the string.
"""


def z_algorithm(s: str) -> list[int]:
    """
    Compute the Z-array for a string.

    Args:
        s: Input string.

    Returns:
        A list where Z[i] is the length of the longest substring starting
        at i that matches the prefix of s.
    """
    if not s:
        return []

    z = [0] * len(s)
    left = 0
    right = 0

    for k in range(1, len(s)):
        if k > right:
            n = 0

            while k + n < len(s) and s[n] == s[k + n]:
                n += 1

            z[k] = n

            if n > 0:
                left = k
                right = k + n - 1
        else:
            mirrored_index = k - left
            remaining_box_length = right - k + 1

            if z[mirrored_index] < remaining_box_length:
                z[k] = z[mirrored_index]
            else:
                i = right + 1

                while i < len(s) and s[i] == s[i - k]:
                    i += 1

                z[k] = i - k
                left = k
                right = i - 1

    return z


def _choose_separator(text: str, pattern: str) -> str:
    """
    Choose a separator character that does not appear in the text or pattern.
    """
    for separator in ["$", "#", "@", "|", "%", "&"]:
        if separator not in text and separator not in pattern:
            return separator

    raise ValueError("Could not find a safe separator character.")


def z_search(text: str, pattern: str) -> list[int]:
    """
    Find all occurrences of a pattern in a text using the Z-algorithm.

    Args:
        text: Text to search within.
        pattern: Pattern to search for.

    Returns:
        A list of zero-based starting positions where the pattern occurs.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    separator = _choose_separator(text, pattern)
    combined = pattern + separator + text
    z = z_algorithm(combined)
    pattern_length = len(pattern)

    matches = []

    for i in range(pattern_length + 1, len(combined)):
        if z[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches


def to_rosalind_positions(indices: list[int]) -> list[int]:
    """
    Convert zero-based Python indices to one-based Rosalind-style positions.
    """
    return [index + 1 for index in indices]


if __name__ == "__main__":
    sample_text = "ACGTACGTGACG"
    sample_pattern = "ACG"

    zero_based_matches = z_search(sample_text, sample_pattern)
    one_based_matches = to_rosalind_positions(zero_based_matches)

    print("Z-array:", z_algorithm(sample_text))
    print("Zero-based matches:", zero_based_matches)
    print("Rosalind-style one-based matches:", one_based_matches)
