from random import randint
from datetime import datetime
from string import ascii_letters, digits


def random_string(max_length_of_string):
    # NB This does not generate non-english charaters
    chars = ascii_letters + digits + ' '
    return ''.join([chars[randint(0, len(chars) - 1)] for x in range(randint(1, max_length_of_string))])


def random_date():
    return datetime.fromordinal(randint(500000, 800000))
