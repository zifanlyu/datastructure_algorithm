import datetime as dt
import subprocess
import sys

import pytest

from dsa.cli import REDO_GAPS, due_dates, main, new_problem, parse_slug, read_log

D0 = dt.date(2026, 10, 1)


def day(n):
    return (D0 + dt.timedelta(days=n)).isoformat()


def rows(*attempts):
    return [{"date": day(n), "id": str(pid), "result": result} for n, pid, result in attempts]


@pytest.mark.parametrize(
    "text",
    [
        "top-k-frequent-elements",
        "https://leetcode.com/problems/top-k-frequent-elements/",
        "https://leetcode.com/problems/top-k-frequent-elements/description/",
    ],
)
def test_parse_slug(text):
    assert parse_slug(text) == "top-k-frequent-elements"


@pytest.mark.parametrize("text", ["Top K", "two_sum", "", "-a"])
def test_parse_slug_rejects(text):
    with pytest.raises(ValueError):
        parse_slug(text)


def test_new_problem_layout_and_no_overwrite(tmp_path):
    solution, test = new_problem(tmp_path, 3, "longest-substring-without-repeating-characters", 3)
    week = tmp_path / "leetcode" / "w03"
    assert solution == week / "lc0003_longest_substring_without_repeating_characters.py"
    assert test == week / "test_lc0003_longest_substring_without_repeating_characters.py"
    assert (tmp_path / "leetcode" / "__init__.py").exists()
    assert (week / "__init__.py").exists()
    assert "https://leetcode.com/problems/longest-substring-without-repeating-characters/" in (
        solution.read_text(encoding="utf-8")
    )
    assert test.read_text(encoding="utf-8").startswith(
        "from leetcode.w03.lc0003_longest_substring_without_repeating_characters import Solution"
    )
    with pytest.raises(FileExistsError):
        new_problem(tmp_path, 3, "longest-substring-without-repeating-characters", 3)


def test_generated_test_imports_and_fails_until_written(tmp_path):
    new_problem(tmp_path, 1, "two-sum", 1)
    # Placeholder test must fail (not pass, not error on import) so an unwritten test is visible.
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "leetcode"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert "1 failed" in result.stdout, result.stdout + result.stderr
    assert "NotImplementedError" in result.stdout


def test_clean_first_time_never_due():
    assert due_dates(rows((0, 1, "clean"))) == {}


def test_miss_schedules_redos_at_growing_gaps():
    history = [(0, 1, "failed")]
    for k, gap in enumerate(REDO_GAPS):
        expected_day = history[-1][0] + gap
        assert due_dates(rows(*history)) == {1: D0 + dt.timedelta(days=expected_day)}, k
        history.append((expected_day, 1, "clean"))
    assert due_dates(rows(*history)) == {}


def test_new_miss_resets_schedule():
    history = rows((0, 1, "hint"), (3, 1, "clean"), (5, 1, "failed"))
    assert due_dates(history) == {1: D0 + dt.timedelta(days=5 + REDO_GAPS[0])}


def test_log_order_irrelevant_across_days():
    a = rows((0, 1, "failed"), (3, 1, "clean"))
    assert due_dates(a) == due_dates(a[::-1])


def test_log_then_due_end_to_end(tmp_path, capsys):
    (tmp_path / "log.csv").write_text("date,id,result,minutes,pattern,note\n", encoding="utf-8")
    new_problem(tmp_path, 347, "top-k-frequent-elements", 2)
    assert main(["log", "347", "hint", "--minutes", "30", "--note", "buckets, by count", "--date", day(0)], tmp_path) == 0
    assert main(["log", "1", "clean", "--date", day(0)], tmp_path) == 0
    logged = read_log(tmp_path / "log.csv")
    assert [r["id"] for r in logged] == ["347", "1"]
    assert logged[0]["note"] == "buckets, by count"  # comma survives CSV quoting
    assert logged[1]["minutes"] == ""
    capsys.readouterr()

    main(["due", "--today", day(2)], tmp_path)
    assert capsys.readouterr().out.strip() == f"nothing due; next: 347 on {day(3)}"

    main(["due", "--today", day(3)], tmp_path)
    assert capsys.readouterr().out.strip() == (
        f"{day(3)}   347  leetcode/w02/lc0347_top_k_frequent_elements.py"
    )


def test_new_reports_existing_file(tmp_path, capsys):
    assert main(["new", "1", "two-sum", "--week", "1"], tmp_path) == 0
    assert main(["new", "1", "two-sum", "--week", "1"], tmp_path) == 1
    assert "already exists" in capsys.readouterr().out
