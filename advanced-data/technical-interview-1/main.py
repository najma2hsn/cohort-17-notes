"""Solution for the Woof Decoder puzzle."""


def translate_sequence_to_letter(seq: list[str]) -> str:
    """Returns a single character from a list of valid woofs."""
    
    if len(seq) == 0:
        raise ValueError("Empty sequence.")

    # Count sequences
    index = len(seq)

    # Get letter by index
    return "abcdefghijklmnopqrstuvwxyz"[index - 1]


def is_valid_woof(possible_woof: str) -> bool:
    """Returns true if a str is a valid woof."""
    
    necessary = ["w", "o", "o", "f"]

    for char in possible_woof.lower():
        if char == necessary[0]:
            necessary.pop(0)

    return len(necessary) == 0


if __name__ == "__main__":

    pass 