def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return the set of letters found in phrase."""
    return set(letters).intersection(set(phrase))


def say_hello():
    return 'Hello!!'
