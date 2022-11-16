from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BinaryFraction:
    int_part: str | None
    periodical_part: str | None
    non_periodical_part: str | None