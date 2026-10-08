"""Binary min-heap from scratch.

Array layout: the children of index i are 2i + 1 and 2i + 2, and every element
is <= its children. ``heapq`` uses the same layout on a plain list.

    MinHeap(items)  build in O(n)
    push(x)         O(log n)
    pop()           O(log n); remove and return the minimum; IndexError if empty
    peek()          O(1); return the minimum; IndexError if empty
    len(h)

Keep the array in ``self.a``; the tests check the heap property on it.
"""

from typing import Iterable, List


class MinHeap:
    def __init__(self, items: Iterable[int] = ()) -> None:
        self.a: List[int] = list(items)
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.a)
