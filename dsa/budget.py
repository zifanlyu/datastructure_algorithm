"""Comparison budgets: fail fast, with a clear message, where LeetCode would time out.

    budget = ComparisonBudget(limit=60 * n)
    result = kth_largest(budget.wrap(nums), k)   # raises BudgetExceeded past the limit

Wrapped values are ints whose comparisons with other ints are counted. Values
produced by arithmetic (``-x``, ``x + 1``) are plain ints and are not counted.
"""

from __future__ import annotations

import operator
from collections.abc import Iterable


class BudgetExceeded(AssertionError):
    pass


class ComparisonBudget:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.used = 0

    def wrap(self, values: Iterable[int]) -> list[int]:
        return [_Counted(v, self) for v in values]

    def charge(self) -> None:
        self.used += 1
        if self.used > self.limit:
            raise BudgetExceeded(
                f"more than {self.limit} comparisons: the algorithm is asymptotically "
                "slower than required on this input"
            )


def _counted(op):
    def compare(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self._budget.charge()
        return op(int(self), int(other))

    return compare


class _Counted(int):
    def __new__(cls, value: int, budget: ComparisonBudget) -> _Counted:
        obj = super().__new__(cls, value)
        obj._budget = budget
        return obj

    __lt__ = _counted(operator.lt)
    __le__ = _counted(operator.le)
    __gt__ = _counted(operator.gt)
    __ge__ = _counted(operator.ge)
    __eq__ = _counted(operator.eq)
    __ne__ = _counted(operator.ne)
    __hash__ = int.__hash__
