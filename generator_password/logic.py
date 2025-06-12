import random
from config import UPPERCASE, LOWERCASE, DIGITS, SPECIALS

def generate_password(length, use_upper, use_lower, use_digits, use_specials):
    chars = ""
    if use_upper:
        chars += UPPERCASE
    if use_lower:
        chars += LOWERCASE
    if use_digits:
        chars += DIGITS
    if use_specials:
        chars += SPECIALS

    if not chars:
        raise ValueError("Не вибрано жодного типу символів")

    return ''.join(random.choice(chars) for _ in range(length))
