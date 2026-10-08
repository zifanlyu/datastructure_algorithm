from dsa.stress import stress
from leetcode.w01.lc0001_two_sum import Solution


def is_valid_pair(args, result):
    nums, target = args
    if not isinstance(result, (list, tuple)) or len(result) != 2:
        return False
    i, j = result
    n = len(nums)
    return i != j and 0 <= i < n and 0 <= j < n and nums[i] + nums[j] == target


def planted_pair(rng):
    nums = rng.choices(range(-10, 11), k=rng.randint(2, 12))
    i, j = rng.sample(range(len(nums)), 2)
    return nums, nums[i] + nums[j]


def test_examples():
    s = Solution()
    assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(s.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(s.twoSum([3, 3], 6)) == [0, 1]  # same value, different indices


def test_edges():
    s = Solution()
    assert sorted(s.twoSum([-3, 4, 3, 90], 0)) == [0, 2]  # negatives
    assert sorted(s.twoSum([0, 4, 3, 0], 0)) == [0, 3]  # zero target
    assert sorted(s.twoSum([1, 5, 3], 6)) == [0, 1]  # 3 + 3 is not allowed: one index used twice


def test_random():
    stress(lambda nums, target: Solution().twoSum(nums, target), planted_pair, check=is_valid_pair)
