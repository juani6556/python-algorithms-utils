"""
Tower of Hanoi recursive solver.
Returns a list of moves required to move n disks.
"""

from typing import List, Tuple


def hanoi(n: int, source: str, auxiliary: str, target: str) -> List[Tuple[str, str]]:
    """Return the sequence of moves needed to solve Tower of Hanoi."""
    if n <= 0:
        return []

    moves = hanoi(n - 1, source, target, auxiliary)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, auxiliary, source, target))

    return moves


if __name__ == "__main__":
    steps = hanoi(3, "A", "B", "C")
    print(steps)
