import random
import string

LIBRARY_GUIDS = [
    '8DFC621C-375D-EB11-A864-00155DAD2A3A',
    '4656CA50-715C-EB11-A864-00155DAD2A3A',
    '440CC25C-715C-EB11-A864-00155DAD2A3A',
    '1022C256-715C-EB11-A864-00155DAD2A3A',
]

ISBN_SEQUENCE = list(range(30000, 20000, -1))

letters = string.ascii_lowercase


def get_random_existing_library_guid():
    return random.choice(LIBRARY_GUIDS)


def get_next_isbn():
    return str(ISBN_SEQUENCE.pop())


def get_random_book_title():
    return ''.join(random.choice(letters) for i in range(10))
