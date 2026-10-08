"""Randomized differential testing: compare a solution with a brute force."""

from __future__ import annotations

import copy
import random
from collections.abc import Callable, Sequence
from typing import Any


def stress(
    candidate: Callable[..., Any],
    gen: Callable[[random.Random], Sequence[Any]],
    *,
    oracle: Callable[..., Any] | None = None,
    check: Callable[[tuple[Any, ...], Any], bool] | None = None,
    cases: int = 300,
    seed: int = 0,
) -> None:
    """Run ``candidate`` on ``cases`` random inputs drawn from ``gen``.

    ``gen(rng)`` returns the positional arguments for one call. Each result is
    judged either against ``oracle`` called on the same arguments (compared
    with ``==``) or by ``check(args, result)``; pass exactly one of the two.
    Every call receives a deep copy of the arguments, so a solution that
    mutates its input cannot affect the oracle or the reported input.

    The run is a deterministic function of ``seed``. Raises AssertionError
    naming the first failing case and its input.
    """
    if (oracle is None) == (check is None):
        raise TypeError("pass exactly one of oracle= or check=")
    rng = random.Random(seed)
    for i in range(cases):
        args = tuple(gen(rng))
        where = f"case {i} (seed={seed}), input {args!r}"
        try:
            got = candidate(*copy.deepcopy(args))
        except Exception as e:
            raise AssertionError(f"{where}\n  raised {type(e).__name__}: {e}") from e
        if oracle is not None:
            expected = oracle(*copy.deepcopy(args))
            if got != expected:
                raise AssertionError(f"{where}\n  expected {expected!r}\n  got      {got!r}")
        elif not check(args, got):
            raise AssertionError(f"{where}\n  invalid result {got!r}")
