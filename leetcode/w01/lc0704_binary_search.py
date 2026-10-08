"""LeetCode 704. Binary Search

https://leetcode.com/problems/binary-search/

Return the index of ``target`` in the ascending, duplicate-free list ``nums``,
or -1 if it is absent, in O(log n) time.

Also write, without ``bisect``, the two primitives most binary searches reduce
to. For an ascending list ``a`` that may contain duplicates:

    lower_bound(a, x): first index i with a[i] >= x   (bisect.bisect_left)
    upper_bound(a, x): first index i with a[i] >  x   (bisect.bisect_right)

Both return len(a) when no such index exists.

Pattern:
Time / space:
"""

from typing import List


def lower_bound(a: List[int], x: int) -> int:
    raise NotImplementedError


def upper_bound(a: List[int], x: int) -> int:
    raise NotImplementedError


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError
