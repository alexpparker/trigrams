"""a module that takes in a text file and outputs a trigrams story of length n words"""
from typing import Dict
from random import choice
import sys


def main(path: str, words_to_generate: int):  # pragma: no cover
    generated_text = "..."
    generated_text_list = []
    trigram_dict = create_trigram_dict(path)
    starter_words = choose_starter_words(trigram_dict)
    generated_text_list.extend(starter_words.split())

    for i in range(words_to_generate - 2):
        key = " ".join(generated_text_list[-2:])
        try:
            generated_text_list.append(generate_next_word(key, trigram_dict))
        except KeyError:
            continue

    generated_text += " ".join(generated_text_list) + "..."
    return generated_text


def create_trigram_dict(path: str):
    """Takes in a file path and outputs a trigram dictionary created from the file"""
    trigram_dict = {}
    with open(path) as book:
        words = book.read().split()
        for index, word in enumerate(words[:-2]):
            trigram_dict.setdefault(words[index] + " " + words[index+1], [])
            trigram_dict[words[index] + " " + words[index+1]].append(words[index + 2])
    return trigram_dict


def choose_starter_words(trigram_dict: Dict):
    """Takes in a trigram dictionary and returns the key string with the largest options"""
    max_key_len = 0
    starter_key = ""
    for k, v in trigram_dict.items():
        if len(v) > max_key_len:
            max_key_len = len(v)
            starter_key = k
    return starter_key


def generate_next_word(starter_words: str, trigram_dict: Dict):  # pragma: no cover
    """Takes in the key string containing the two starter words and dictionary to use, then returns the next word"""
    return choice(trigram_dict[starter_words])


if __name__ == "__main__":  # pragma: no cover
    print(main(sys.argv[1], int(sys.argv[2])))

# sherlock = "../texts/sherlock.txt"

# main(sherlock, 200)
