import heapq

import pytest

from dsa.stress import stress
from leetcode.w01.min_heap import MinHeap


def is_heap(a):
    return all(a[(i - 1) // 2] <= a[i] for i in range(1, len(a)))


def ops(rng):
    initial = rng.choices(range(10), k=rng.randint(0, 8))
    sequence = [
        ("push", rng.randint(0, 9)) if rng.random() < 0.5 else ("pop", None)
        for _ in range(rng.randint(0, 20))
    ]
    return initial, sequence


def run_min_heap(initial, sequence):
    h = MinHeap(initial)
    out = []
    for op, x in sequence:
        if op == "push":
            h.push(x)
        else:
            try:
                out.append(h.pop())
            except IndexError:
                out.append("empty")
        if not is_heap(h.a):
            return out + ["heap property broken", list(h.a)]
    return out + [len(h)]


def run_heapq(initial, sequence):
    a = list(initial)
    heapq.heapify(a)
    out = []
    for op, x in sequence:
        if op == "push":
            heapq.heappush(a, x)
        else:
            out.append(heapq.heappop(a) if a else "empty")
    return out + [len(a)]


def test_construction_gives_heap():
    for items in ([], [1], list(range(20)), list(range(20, 0, -1)), [3, 1, 3, 1, 2]):
        h = MinHeap(items)
        assert sorted(h.a) == sorted(items)
        assert is_heap(h.a), items


def test_peek_and_empty():
    h = MinHeap([4, 2, 9])
    assert h.peek() == 2
    assert len(h) == 3
    assert [h.pop() for _ in range(3)] == [2, 4, 9]
    with pytest.raises(IndexError):
        h.pop()
    with pytest.raises(IndexError):
        h.peek()


def test_random_operations_match_heapq():
    stress(run_min_heap, ops, oracle=run_heapq)
