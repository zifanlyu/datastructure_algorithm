import pytest

from dsa.stress import stress


def int_list(rng):
    return (rng.choices(range(-3, 4), k=rng.randint(0, 6)),)


def test_correct_candidate_passes():
    stress(lambda xs: sorted(xs), int_list, oracle=sorted)


def test_wrong_candidate_reports_case_and_input():
    with pytest.raises(AssertionError, match=r"case \d+ \(seed=0\), input \(\[.*\],\)"):
        stress(lambda xs: xs, int_list, oracle=sorted)


def test_exception_in_candidate_is_reported_with_input():
    def crash(xs):
        raise RecursionError("too deep")

    with pytest.raises(AssertionError, match="raised RecursionError: too deep"):
        stress(crash, int_list, oracle=sorted)


def test_check_mode():
    def is_sorted_permutation(args, result):
        return result == sorted(args[0])

    stress(lambda xs: sorted(xs), int_list, check=is_sorted_permutation)
    with pytest.raises(AssertionError, match="invalid result"):
        stress(lambda xs: xs[::-1], int_list, check=is_sorted_permutation)


def test_requires_exactly_one_judge():
    with pytest.raises(TypeError):
        stress(sorted, int_list)
    with pytest.raises(TypeError):
        stress(sorted, int_list, oracle=sorted, check=lambda args, r: True)


def test_same_seed_same_failure():
    messages = []
    for _ in range(2):
        with pytest.raises(AssertionError) as info:
            stress(lambda xs: xs, int_list, oracle=sorted, seed=7)
        messages.append(str(info.value))
    assert messages[0] == messages[1]


def test_mutating_candidate_does_not_affect_oracle_or_report():
    def sort_in_place_then_corrupt(xs):
        xs.sort()
        xs.append(99)
        return xs[:-1]

    stress(sort_in_place_then_corrupt, int_list, oracle=sorted)
