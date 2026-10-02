def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    char_counts = {}
    for char in magazine:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in ransomNote:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True
