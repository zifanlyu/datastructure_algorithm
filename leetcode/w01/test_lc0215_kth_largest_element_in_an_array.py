import math
import random

import pytest

from dsa.budget import ComparisonBudget
from dsa.stress import stress
from leetcode.w01.lc0215_kth_largest_element_in_an_array import (
    Solution,
    kth_largest_heap,
    kth_largest_quickselect,
)

METHODS = [kth_largest_heap, kth_largest_quickselect]
IDS = ["heap", "quickselect"]

N = 20000
_rng = random.Random(2)
LARGE = {
    "random": [_rng.randint(-(10**4), 10**4) for _ in range(N)],
    "sorted": list(range(N)),
    "all equal": [1] * N,
}
# Several times what O(n log k) and expected O(n) need; quadratic exceeds them fast.
COMPARISON_LIMIT = {"heap": int(20 * N * math.log2(N)), "quickselect": 60 * N}


def brute_force(nums, k):
    return sorted(nums, reverse=True)[k - 1]


def list_and_k(rng):
    nums = rng.choices(range(-5, 6), k=rng.randint(1, 20))
    return nums, rng.randint(1, len(nums))


def test_examples():
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


@pytest.mark.parametrize("method", METHODS, ids=IDS)
def test_edges(method):
    assert method([7], 1) == 7
    assert method([3, 3, 1], 2) == 3  # duplicates count
    assert method([-1, -5, -3], 3) == -5  # k = n is the minimum


@pytest.mark.parametrize("method", METHODS, ids=IDS)
def test_random(method):
    stress(method, list_and_k, oracle=brute_force)


@pytest.mark.parametrize("method,limit", list(zip(METHODS, COMPARISON_LIMIT.values())), ids=IDS)
@pytest.mark.parametrize("name", list(LARGE))
def test_large_inputs(method, limit, name):
    nums = LARGE[name]
    for k in (1, N // 2, N):
        result = method(ComparisonBudget(limit).wrap(nums), k)
        assert int(result) == brute_force(nums, k), k
