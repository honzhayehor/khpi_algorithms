import random
import pytest

from euler.tasks.exercise_22 import (
    DEFAULT_NAMES_FILE,
    load_names,
    name_score,
    name_to_chars,
    parse_names,
    letter_to_num,
    sum_of_name_letters,
    total_name_scores,
)

NAMES_FILE = DEFAULT_NAMES_FILE


def test_letter_to_num():
    assert letter_to_num("a") == 1
    assert letter_to_num("A") == 1
    assert letter_to_num("Z") == 26


def test_name_to_chars_and_sum_of_name_letters():
    assert name_to_chars("COLIN") == ["C", "O", "L", "I", "N"]
    assert sum_of_name_letters("COLIN") == 53


def test_name_score_example_from_problem():
    assert name_score("COLIN", 938) == 49714


def test_parse_names_strips_quotes_and_whitespace():
    assert parse_names('"MARY", "PATRICIA" ,"LINDA"\n') == ["MARY", "PATRICIA", "LINDA"]


def test_parse_names_empty_text():
    assert parse_names("") == []


def test_load_names_reads_file(tmp_path):
    file = tmp_path / "names.txt"
    file.write_text('"BOB","ALICE","CAROL"', encoding="utf-8")
    assert load_names(file) == ["BOB", "ALICE", "CAROL"]


def test_total_for_small_list():
    assert total_name_scores(["BOB", "ALICE", "CAROL"]) == 215


def test_input_order_does_not_matter():
    names = ["BOB", "ALICE", "CAROL", "DAVE", "EVE", "FRANK"]
    expected = total_name_scores(names)
    shuffled = names[:]
    random.Random(1).shuffle(shuffled)
    assert total_name_scores(shuffled) == expected


def test_empty_list_scores_zero():
    assert total_name_scores([]) == 0


@pytest.mark.skipif(not NAMES_FILE.exists(), reason="inputs/names.txt not found")
def test_full_answer():
    names = load_names(NAMES_FILE)
    assert len(names) == 5163
    assert total_name_scores(names) == 871198282