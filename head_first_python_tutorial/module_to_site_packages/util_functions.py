# example:
from datetime import date


def print_todays_date():
    date_today = date.today()
    print(date_today)


def convert_number_to_string(n):
    """converting a integer to string"""
    return str(n)


def search_vowels(word):
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_vowels_2(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search_vowels_3(word: str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_vowels_4(word: str) -> bool:
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


# using multiple argument
# search for letters in a given phrase

def search4letters(phrase: str, letters: str):
    """Return a set of the 'letters' found in 'phrase'"""
    return sorted(set(phrase).intersection(set(letters)))


print(search4letters('Paranoid Android', 'aeiou'))
