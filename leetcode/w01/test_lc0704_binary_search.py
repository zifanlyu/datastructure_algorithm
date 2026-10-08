import bisect

from dsa.stress import stress
from leetcode.w01.lc0704_binary_search import Solution, lower_bound, upper_bound


def test_examples():
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_edges():
    s = Solution()
    assert s.search([5], 5) == 0
    assert s.search([5], 4) == -1
    assert s.search([1, 3], 0) == -1  # below every element
    assert s.search([1, 3], 4) == -1  # above every element
    assert s.search([1, 3], 3) == 1  # last index


def distinct_sorted(rng):
    nums = sorted(rng.sample(range(-20, 21), rng.randint(1, 12)))
    return nums, rng.randint(-22, 22)


def sorted_with_duplicates(rng):
    return sorted(rng.choices(range(5), k=rng.randint(0, 10))), rng.randint(-1, 5)


def test_search_random():
    stress(
        lambda nums, target: Solution().search(nums, target),
        distinct_sorted,
        oracle=lambda nums, target: nums.index(target) if target in nums else -1,
    )


def test_lower_bound_random():
    stress(lower_bound, sorted_with_duplicates, oracle=bisect.bisect_left)


def test_upper_bound_random():
    stress(upper_bound, sorted_with_duplicates, oracle=bisect.bisect_right)
