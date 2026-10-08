# Interview practice

The week-by-week plan is in [PLAN.md](PLAN.md). This repository holds the solutions and
their tests.

## Setup

```
uv sync
```

## This week

```
uv run pytest leetcode/w01
```

Week 1 contains stubs that raise `NotImplementedError`, so every test fails until you fill
them in. Each stub's docstring states what to implement.

## Daily workflow

```
uv run python -m dsa new 347 top-k-frequent-elements --week 2
uv run python -m dsa log 347 hint --minutes 30 --pattern "bucket sort" --note "bucket by count"
uv run python -m dsa due
```

- `new` creates `leetcode/w02/lc0347_top_k_frequent_elements.py` and its test. It accepts
  the slug or the problem URL, and never overwrites. The placeholder test fails until you
  write it.
- `log` appends an attempt to `log.csv`. The result is `clean`, `hint` or `failed`.
- `due` lists the problems to redo today. A problem with a `hint` or `failed` attempt comes
  back 3, 7 and 21 days later, until it has been solved cleanly three times in a row.

## Layout

- `leetcode/wNN/`: `lcNNNN_slug.py` and `test_lcNNNN_slug.py`. Solutions use LeetCode's
  `class Solution` signatures, so they paste straight into the site.
- `probability/`, `ml/`: the code exercises from PLAN.md, as `<name>.py` with
  `test_<name>.py` next to it.
- `dsa/stress.py`: compares a solution with a brute force on random inputs from a fixed
  seed, and reports the first failing input.
- `dsa/budget.py`: counts comparisons, so a quadratic algorithm fails fast in a test
  instead of timing out on LeetCode.
- `log.csv`: one row per attempt.

## Check everything

```
uv run pytest
```
