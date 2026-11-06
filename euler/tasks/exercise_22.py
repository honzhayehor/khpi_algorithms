from pathlib import Path

DEFAULT_NAMES_FILE = Path.cwd() / "euler" / "inputs" / "names.txt"

def letter_to_num(char: str):
    return ord(char.lower()) - ord('a') + 1

def name_to_chars(name: str):
    return [char for char in name]

def sum_of_name_letters(name: str):
    chars = name_to_chars(name)
    return sum([letter_to_num(char) for char in chars])

def parse_names(text: str) -> list:
    names = [part.strip().strip('"') for part in text.split(",")]
    return [name for name in names if name]


def load_names(path=DEFAULT_NAMES_FILE) -> list:
    return parse_names(Path(path).read_text(encoding="utf-8"))


def name_score(name: str, position: int) -> int:
    return sum_of_name_letters(name) * position


def total_name_scores(names: list) -> int:
    return sum(
        name_score(name, position)
        for position, name in enumerate(sorted(names), start=1)
    )
