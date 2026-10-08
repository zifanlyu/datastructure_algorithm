"""LeetCode 912. Sort an Array

https://leetcode.com/problems/sort-an-array/

Sort ``nums`` ascending in O(n log n) time without the built-in sort. Write
both algorithms; ``sortArray`` may call either. Each returns the sorted list
and may modify its argument.

merge_sort: O(n log n) in the worst case.
quicksort:  random pivot, O(n log n) expected. It must also handle inputs in
            which most keys are equal (see test_large_inputs).

Pattern:
Time / space:
"""

from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    raise NotImplementedError


def quicksort(nums: List[int]) -> List[int]:
    raise NotImplementedError


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        raise NotImplementedError
