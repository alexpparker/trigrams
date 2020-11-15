"""Tests for the Trigrams function"""
import pytest
from trigrams import choose_starter_words, create_trigram_dict


CREATE_PARAMS_TABLE = [
    ("texts/sherlock_small.txt", "the dark", ["incidents"]),
    ("texts/sherlock_small.txt", "He was", ["pacing", "at"]),
    ("texts/sherlock_small.txt", "I was", ["seized"])
]

STARTER_PARAMS_TABLE = [
    ({"two words": ["this", "has", "many", "values"]}, "two words"),
    ({"hey hey": ["listen", "navi"], "nope": []}, "hey hey"),
    ({"one number": ["two"], "this thing": ["thing", "things"]}, "this thing")
]


@pytest.mark.parametrize("text_file, key, value", CREATE_PARAMS_TABLE)
def test_create_diagram_dict(text_file, key, value):
    assert create_trigram_dict(text_file)[key] == value


@pytest.mark.parametrize("tri_dict, result", STARTER_PARAMS_TABLE)
def test_choose_starter_words(tri_dict, result):
    assert choose_starter_words(tri_dict) == result
