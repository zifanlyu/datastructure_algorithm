"""Problem workflow: scaffold a problem, log an attempt, list the redos due.

    uv run python -m dsa new 347 top-k-frequent-elements --week 2
    uv run python -m dsa log 347 hint --minutes 30 --pattern "bucket sort" --note "..."
    uv run python -m dsa due
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG_FIELDS = ["date", "id", "result", "minutes", "pattern", "note"]
RESULTS = ("clean", "hint", "failed")
# Days until the next redo, indexed by the number of clean attempts since the last miss.
REDO_GAPS = (3, 7, 21)

SOLUTION_TEMPLATE = '''"""LeetCode {pid}. {title}

https://leetcode.com/problems/{slug}/

Pattern:
Time / space:
"""

from typing import List, Optional  # noqa: F401  (LeetCode signatures use these)


class Solution:
    # Replace with the method signature from the problem page.
    def solve(self) -> None:
        raise NotImplementedError
'''

TEST_TEMPLATE = '''from {package}.{module} import Solution


def test_examples():
    s = Solution()
    raise NotImplementedError("turn the examples on the problem page into asserts on s")


# Then add edge cases (empty, single element, duplicates, negatives) and a
# randomized comparison against a brute force:
#     from dsa.stress import stress
'''


def parse_slug(text: str) -> str:
    """Accept a slug or a problem URL; return the slug."""
    m = re.search(r"/problems/([^/]+)", text)
    slug = m.group(1) if m else text.strip("/")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        raise ValueError(f"not a LeetCode slug: {text!r}")
    return slug


def module_name(pid: int, slug: str) -> str:
    return f"lc{pid:04d}_{slug.replace('-', '_')}"


def new_problem(root: Path, pid: int, slug: str, week: int) -> tuple[Path, Path]:
    """Write a solution stub and its test into leetcode/wNN/; never overwrite."""
    module = module_name(pid, slug)
    week_dir = root / "leetcode" / f"w{week:02d}"
    solution = week_dir / f"{module}.py"
    test = week_dir / f"test_{module}.py"
    for path in (solution, test):
        if path.exists():
            raise FileExistsError(f"{path} already exists")
    week_dir.mkdir(parents=True, exist_ok=True)
    for package in (root / "leetcode", week_dir):
        (package / "__init__.py").touch()
    title = " ".join(word.capitalize() for word in slug.split("-"))
    solution.write_text(SOLUTION_TEMPLATE.format(pid=pid, title=title, slug=slug), encoding="utf-8")
    test.write_text(
        TEST_TEMPLATE.format(package=f"leetcode.w{week:02d}", module=module), encoding="utf-8"
    )
    return solution, test


def read_log(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_log(path: Path, row: dict[str, object]) -> None:
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def due_dates(rows: list[dict[str, str]]) -> dict[int, dt.date]:
    """Next redo date for every problem that still needs one.

    A problem needs redos once any attempt is a miss (hint or failed). After the
    last miss it comes back REDO_GAPS[k] days after the latest attempt, where k
    is the number of clean attempts since that miss; after len(REDO_GAPS) clean
    attempts it is done. A problem solved cleanly on every attempt never returns.
    """
    attempts: dict[int, list[tuple[dt.date, str]]] = {}
    for row in rows:
        attempts.setdefault(int(row["id"]), []).append(
            (dt.date.fromisoformat(row["date"]), row["result"])
        )
    out = {}
    for pid, history in attempts.items():
        history.sort(key=lambda attempt: attempt[0])  # stable: same-day attempts keep log order
        misses = [i for i, (_, result) in enumerate(history) if result != "clean"]
        if not misses:
            continue
        clean_since = len(history) - 1 - misses[-1]
        if clean_since < len(REDO_GAPS):
            out[pid] = history[-1][0] + dt.timedelta(days=REDO_GAPS[clean_since])
    return out


def find_solution(root: Path, pid: int) -> str:
    matches = sorted((root / "leetcode").glob(f"w*/lc{pid:04d}_*.py"))
    return ", ".join(p.relative_to(root).as_posix() for p in matches)


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(prog="python -m dsa")
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="create a solution stub and its test")
    p_new.add_argument("id", type=int, help="LeetCode problem number")
    p_new.add_argument("slug", help="slug or URL, e.g. top-k-frequent-elements")
    p_new.add_argument("--week", type=int, required=True, help="plan week, 1-15")

    p_log = sub.add_parser("log", help="record an attempt in log.csv")
    p_log.add_argument("id", type=int)
    p_log.add_argument("result", choices=RESULTS)
    p_log.add_argument("--minutes", type=int)
    p_log.add_argument("--pattern", default="")
    p_log.add_argument("--note", default="", help="key insight or mistake, one line")
    p_log.add_argument("--date", type=dt.date.fromisoformat, default=dt.date.today())

    p_due = sub.add_parser("due", help="list problems due for a redo")
    p_due.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())

    args = parser.parse_args(argv)
    log_path = root / "log.csv"

    if args.command == "new":
        try:
            created = new_problem(root, args.id, parse_slug(args.slug), args.week)
        except (ValueError, FileExistsError) as e:
            print(f"error: {e}")
            return 1
        for path in created:
            print(path.relative_to(root).as_posix())
    elif args.command == "log":
        append_log(
            log_path,
            {
                "date": args.date.isoformat(),
                "id": args.id,
                "result": args.result,
                "minutes": "" if args.minutes is None else args.minutes,
                "pattern": args.pattern,
                "note": args.note,
            },
        )
        print(f"logged {args.id} {args.result} on {args.date.isoformat()}")
    elif args.command == "due":
        upcoming = sorted(due_dates(read_log(log_path)).items(), key=lambda item: (item[1], item[0]))
        now = [(pid, day) for pid, day in upcoming if day <= args.today]
        for pid, day in now:
            print(f"{day.isoformat()}  {pid:>4}  {find_solution(root, pid)}")
        if not now:
            later = [(pid, day) for pid, day in upcoming if day > args.today]
            print(f"nothing due; next: {later[0][0]} on {later[0][1].isoformat()}" if later else "nothing due")
    return 0
