"""LeetCode 215. Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/

Return the k-th largest element of ``nums``, 1 <= k <= len(nums), counting
duplicates: the 2nd largest of [3, 3, 1] is 3. Solve it twice:

kth_largest_heap:        with heapq, O(n log k) time, O(k) extra space.
kth_largest_quickselect: random pivot, O(n) expected. It must also handle
                         inputs in which most keys are equal (see the test).

Pattern:
Time / space:
"""

from typing import List


def kth_largest_heap(nums: List[int], k: int) -> int:
    raise NotImplementedError


def kth_largest_quickselect(nums: List[int], k: int) -> int:
    raise NotImplementedError


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        raise NotImplementedError
