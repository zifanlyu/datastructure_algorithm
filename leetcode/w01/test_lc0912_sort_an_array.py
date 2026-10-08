import math
import random

import pytest

from dsa.budget import ComparisonBudget
from dsa.stress import stress
from leetcode.w01.lc0912_sort_an_array import Solution, merge_sort, quicksort

N = 5000
_rng = random.Random(1)
LARGE = {
    "random": [_rng.randint(-(10**9), 10**9) for _ in range(N)],
    "sorted": list(range(N)),
    "reversed": list(range(N, 0, -1)),
    "all equal": [7] * N,
}
# About five times what a correct O(n log n) sort needs; a quadratic one exceeds it fast.
COMPARISON_LIMIT = int(20 * N * math.log2(N))


def small_list(rng):
    return (rng.choices(range(-5, 6), k=rng.randint(0, 30)),)


def test_examples():
    s = Solution()
    assert s.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]


@pytest.mark.parametrize("sort", [merge_sort, quicksort], ids=["merge_sort", "quicksort"])
def test_random(sort):
    stress(sort, small_list, oracle=sorted)


# LeetCode's hidden tests include inputs like these: a deterministic pivot is
# quadratic on "sorted", and a two-way partition is quadratic on "all equal".
@pytest.mark.parametrize("sort", [merge_sort, quicksort], ids=["merge_sort", "quicksort"])
@pytest.mark.parametrize("name", list(LARGE))
def test_large_inputs(sort, name):
    result = sort(ComparisonBudget(COMPARISON_LIMIT).wrap(LARGE[name]))
    assert [int(x) for x in result] == sorted(LARGE[name])
