import heapq

import pytest

from dsa.budget import BudgetExceeded, ComparisonBudget


def test_values_behave_like_ints():
    budget = ComparisonBudget(limit=100)
    a, b = budget.wrap([3, 5])
    assert a < b and b > a and a <= 3 and b >= 5 and a == 3 and a != b
    assert a + b == 8 and -a == -3
    assert {a: "x"}[3] == "x"  # hashable, equal keys collide with plain ints
    assert sorted(budget.wrap([2, 1, 3])) == [1, 2, 3]


def test_counts_comparisons_including_reflected_and_library_calls():
    budget = ComparisonBudget(limit=1000)
    a = budget.wrap([1])[0]
    a < 2
    2 < a  # reflected: int.__lt__ defers to the subclass's __gt__
    assert budget.used == 2
    h = budget.wrap([5, 4, 3, 2, 1])
    heapq.heapify(h)
    assert budget.used > 2


def test_raises_past_limit():
    budget = ComparisonBudget(limit=3)
    a, b = budget.wrap([1, 2])
    for _ in range(3):
        a < b
    with pytest.raises(BudgetExceeded, match="more than 3 comparisons"):
        a < b


def test_quadratic_algorithm_is_caught_linear_is_not():
    n = 2000
    values = list(range(n))

    def quadratic(xs):
        return sum(1 for x in xs for y in xs if x < y)

    def linear(xs):
        return max(xs)

    assert linear(ComparisonBudget(limit=2 * n).wrap(values)) == n - 1
    with pytest.raises(BudgetExceeded):
        quadratic(ComparisonBudget(limit=100 * n).wrap(values))


def test_plain_int_conversion_is_uncounted():
    budget = ComparisonBudget(limit=0)
    xs = budget.wrap([2, 1])
    assert [int(x) for x in xs] == [2, 1]
    assert budget.used == 0
