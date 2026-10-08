from collections import Counter

from dsa.stress import stress
from leetcode.w01.lc0049_group_anagrams import Solution


def canonical(groups):
    return sorted(sorted(g) for g in groups)


def brute_force(strs):
    groups = []
    for s in strs:
        for g in groups:
            if Counter(g[0]) == Counter(s):
                g.append(s)
                break
        else:
            groups.append([s])
    return groups


def random_words(rng):
    return (["".join(rng.choices("abc", k=rng.randint(0, 3))) for _ in range(rng.randint(1, 10))],)


def test_examples():
    s = Solution()
    assert canonical(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == canonical(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert canonical(s.groupAnagrams([""])) == [[""]]
    assert canonical(s.groupAnagrams(["a"])) == [["a"]]


def test_edges():
    s = Solution()
    assert canonical(s.groupAnagrams(["", ""])) == [["", ""]]  # duplicates kept
    assert canonical(s.groupAnagrams(["ab", "ba", "ab"])) == [["ab", "ab", "ba"]]
    assert canonical(s.groupAnagrams(["aab", "abb"])) == [["aab"], ["abb"]]  # same letters, different counts


def test_random():
    stress(
        lambda strs: canonical(Solution().groupAnagrams(strs)),
        random_words,
        oracle=lambda strs: canonical(brute_force(strs)),
    )
