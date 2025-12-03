"""
Secure password generator using Python's secrets module.
"""

import secrets
import string
import re
from typing import Dict


def generate_password(
    length: int = 16,
    min_lower: int = 1,
    min_upper: int = 1,
    min_digits: int = 1,
    min_symbols: int = 1,
) -> str:
    """Generate a cryptographically secure password."""

    alphabet = string.ascii_letters + string.digits + string.punctuation

    patterns = [
        (min_lower, r"[a-z]"),
        (min_upper, r"[A-Z]"),
        (min_digits, r"\d"),
        (min_symbols, f"[{re.escape(string.punctuation)}]"),
    ]

    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(length))

        if all(req <= len(re.findall(pattern, pwd)) for req, pattern in patterns):
            return pwd


if __name__ == "__main__":
    print(generate_password())
