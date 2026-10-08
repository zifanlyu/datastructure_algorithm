# Interview preparation plan

Started 2026-10-08. Commands for the repository are in [README.md](README.md).

## Targets, in priority order

1. **MLE, applied scientist, research scientist** at large firms. Publications are
   direct evidence for these roles.
2. **Quant researcher** (not quant developer). The loop is probability, statistics
   and ML, plus LeetCode-medium coding.
3. **Data scientist, modeling roles only.** Their preparation is a subset of 1 and 2.
   Product-analytics data science is out of scope: its loop centres on SQL and
   product sense.

## Now

- [ ] Move publications near the top of the CV.
- [ ] List target firms and roles, with application status.
- [ ] Apply to quant-researcher roles first: most firms fill them on a rolling basis
      through the autumn.
- [ ] Apply to MLE, applied-scientist and research-scientist roles.
- [ ] Start week 1 below in the same week.

When an online assessment or interview is booked, stop the weekly schedule and
switch to the matching [sprint](#two-week-sprints).

## Time budget

About 12 hours a week. At 20 hours a week the plan takes about 9 weeks.

| Weeks | LeetCode | Probability and statistics | Third track |
|---|---|---|---|
| 1–5 | ~7 h | ~4 h | SQL, ~1 h |
| 6–15 | ~6 h | ~3 h | ML and data code, ~3 h |

LeetCode numbers below are problem IDs. Nearly all are mediums; the hard ones
kept (42, 76, 84, 124, 295, 297) are ones large firms ask often.

## Weekly plan

### Week 1 — Python toolkit, sorting, searching

- [ ] Python toolkit: `deque`, `Counter`, `defaultdict`, `OrderedDict.move_to_end`,
      `heapq` (min-heap only; negate for a max-heap; push `(key, tiebreak, item)`),
      `bisect`, `functools.cache`, the recursion limit of 1000, and hidden O(n)
      operations (`x in list`, slicing, `s += c` in a loop, `list.insert(0, x)`)
- [ ] 704 Binary Search, plus `lower_bound` / `upper_bound` —
      [leetcode/w01/lc0704_binary_search.py](leetcode/w01/lc0704_binary_search.py)
- [ ] 912 Sort an Array: merge sort and quicksort —
      [leetcode/w01/lc0912_sort_an_array.py](leetcode/w01/lc0912_sort_an_array.py)
- [ ] Binary min-heap from scratch —
      [leetcode/w01/min_heap.py](leetcode/w01/min_heap.py)
- [ ] 215 Kth Largest Element in an Array: heap and quickselect —
      [leetcode/w01/lc0215_kth_largest_element_in_an_array.py](leetcode/w01/lc0215_kth_largest_element_in_an_array.py)
- [ ] 1 Two Sum — [leetcode/w01/lc0001_two_sum.py](leetcode/w01/lc0001_two_sum.py)
- [ ] 49 Group Anagrams — [leetcode/w01/lc0049_group_anagrams.py](leetcode/w01/lc0049_group_anagrams.py)
- [ ] Probability: counting, conditional probability, Bayes' rule
- [ ] SQL: `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, joins (LeetCode SQL 50)

### Week 2 — Hashing and prefix sums

- [ ] 347 Top K Frequent Elements
- [ ] 238 Product of Array Except Self
- [ ] 128 Longest Consecutive Sequence
- [ ] 560 Subarray Sum Equals K
- [ ] 525 Contiguous Array
- [ ] 304 Range Sum Query 2D - Immutable
- [ ] Probability: expectation, linearity, indicator variables (coupon collector,
      expected number of fixed points of a random permutation)
- [ ] SQL: subqueries, CTEs, self-joins

### Week 3 — Two pointers and sliding window

- [ ] 167 Two Sum II - Input Array Is Sorted
- [ ] 15 3Sum
- [ ] 11 Container With Most Water
- [ ] 42 Trapping Rain Water
- [ ] 3 Longest Substring Without Repeating Characters
- [ ] 424 Longest Repeating Character Replacement
- [ ] 76 Minimum Window Substring
- [ ] Probability: first-step analysis. Expected flips until HH and until HT, and
      gambler's ruin: simulate each, then solve the linear system exactly with
      `np.linalg.solve` and check that the two agree within the standard error
- [ ] SQL: window functions (`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, running sums)

### Week 4 — Binary search

- [ ] 74 Search a 2D Matrix
- [ ] 33 Search in Rotated Sorted Array
- [ ] 153 Find Minimum in Rotated Sorted Array
- [ ] 875 Koko Eating Bananas
- [ ] 1011 Capacity To Ship Packages Within D Days
- [ ] 981 Time Based Key-Value Store
- [ ] Probability: standard distributions, order statistics, random walks
- [ ] SQL: dates, retention and cohorts, rolling 7-day metrics

### Week 5 — Stacks, monotonic stack and deque

- [ ] 20 Valid Parentheses
- [ ] 155 Min Stack
- [ ] 150 Evaluate Reverse Polish Notation
- [ ] 739 Daily Temperatures
- [ ] 901 Online Stock Span
- [ ] 239 Sliding Window Maximum
- [ ] 84 Largest Rectangle in Histogram
- [ ] Statistics: central limit theorem, standard errors, bootstrap; check the
      coverage of a bootstrap confidence interval by simulation
- [ ] SQL: finish LeetCode SQL 50

### Week 6 — Heaps

- [ ] 703 Kth Largest Element in a Stream
- [ ] 973 K Closest Points to Origin
- [ ] 347 Top K Frequent Elements, heap version
- [ ] 23 Merge k Sorted Lists
- [ ] 621 Task Scheduler
- [ ] 295 Find Median from Data Stream
- [ ] 2034 Stock Price Fluctuation
- [ ] Statistics: hypothesis tests, power and sample size; a permutation test;
      power by simulation; why peeking and multiple testing inflate the
      false-positive rate
- [ ] Data code: pandas for data rounds (groupby-transform, rolling, resample,
      `merge_asof`, replacing loops with vectorized code); Welford's online
      mean and variance, EWMA, rolling max with a deque

### Week 7 — Intervals and greedy

- [ ] 56 Merge Intervals
- [ ] 57 Insert Interval
- [ ] 435 Non-overlapping Intervals
- [ ] 1094 Car Pooling
- [ ] 763 Partition Labels
- [ ] 55 Jump Game
- [ ] 134 Gas Station
- [ ] Statistics: ordinary least squares — derivation, assumptions, standard
      errors, omitted-variable bias
- [ ] ML code: least squares via `lstsq` and via a QR solve, checked against
      statsmodels; logistic regression by gradient descent with a
      finite-difference gradient check

### Week 8 — Dynamic programming I: one dimension and the stock family

- [ ] 70 Climbing Stairs
- [ ] 198 House Robber
- [ ] 53 Maximum Subarray
- [ ] 152 Maximum Product Subarray
- [ ] 121 Best Time to Buy and Sell Stock
- [ ] 122 Best Time to Buy and Sell Stock II
- [ ] 309 Best Time to Buy and Sell Stock with Cooldown
- [ ] 714 Best Time to Buy and Sell Stock with Transaction Fee
- [ ] 322 Coin Change
- [ ] Statistics: ridge and lasso, bias–variance, cross-validation; for time
      series, walk-forward validation, look-ahead bias and leakage
- [ ] ML code: ridge in closed form; k-means with k-means++ initialization;
      kNN with vectorized distances

### Week 9 — Dynamic programming II: two dimensions, knapsack, subsequences

- [ ] 62 Unique Paths
- [ ] 1143 Longest Common Subsequence
- [ ] 72 Edit Distance
- [ ] 300 Longest Increasing Subsequence
- [ ] 416 Partition Equal Subset Sum
- [ ] 518 Coin Change II
- [ ] 139 Word Break
- [ ] Probability DP: 688 Knight Probability in Chessboard, 837 New 21 Game,
      808 Soup Servings, 1227 Airplane Seat Assignment Probability
- [ ] ML code: softmax with cross-entropy, forward and backward; a two-layer MLP
      trained with Adam

### Week 10 — Graphs

- [ ] 200 Number of Islands
- [ ] 994 Rotting Oranges
- [ ] 133 Clone Graph
- [ ] 207 Course Schedule
- [ ] 210 Course Schedule II
- [ ] 547 Number of Provinces
- [ ] 684 Redundant Connection
- [ ] 399 Evaluate Division
- [ ] Probability: Monte Carlo estimates with standard errors; antithetic
      variates and control variates
- [ ] ML code: ROC-AUC via ranks (with ties), precision@k, log-loss

### Week 11 — Randomized algorithms

- [ ] 384 Shuffle an Array
- [ ] 528 Random Pick with Weight
- [ ] 382 Linked List Random Node
- [ ] 398 Random Pick Index
- [ ] 380 Insert Delete GetRandom O(1)
- [ ] 470 Implement Rand10() Using Rand7()
- [ ] 478 Generate Random Point in a Circle
- [ ] Statistics: time series — stationarity, AR(1), autocorrelation
- [ ] ML code: decision-tree split finding (sort, then prefix sums);
      micrograd-style scalar autograd (uses the topological sort from 210)

### Week 12 — Trees

- [ ] 104 Maximum Depth of Binary Tree
- [ ] 543 Diameter of Binary Tree
- [ ] 102 Binary Tree Level Order Traversal
- [ ] 199 Binary Tree Right Side View
- [ ] 98 Validate Binary Search Tree
- [ ] 230 Kth Smallest Element in a BST
- [ ] 236 Lowest Common Ancestor of a Binary Tree
- [ ] 105 Construct Binary Tree from Preorder and Inorder Traversal
- [ ] 124 Binary Tree Maximum Path Sum
- [ ] 297 Serialize and Deserialize Binary Tree
- [ ] Probability: timed mixed puzzle set
- [ ] ML code: multi-head attention with a causal mask, LayerNorm, KV cache

### Week 13 — Linked lists, tries, LRU cache

- [ ] 206 Reverse Linked List
- [ ] 21 Merge Two Sorted Lists
- [ ] 141 Linked List Cycle
- [ ] 143 Reorder List
- [ ] 19 Remove Nth Node From End of List
- [ ] 138 Copy List with Random Pointer
- [ ] 146 LRU Cache
- [ ] 208 Implement Trie (Prefix Tree)
- [ ] 211 Design Add and Search Words Data Structure
- [ ] 1268 Search Suggestions System
- [ ] Probability: timed mixed puzzle set
- [ ] ML code: decoding (greedy, beam search, temperature, top-k, top-p);
      BPE tokenizer (train, encode, decode)

### Week 14 — Backtracking and bit manipulation

- [ ] 78 Subsets
- [ ] 90 Subsets II
- [ ] 46 Permutations
- [ ] 39 Combination Sum
- [ ] 79 Word Search
- [ ] 131 Palindrome Partitioning
- [ ] 136 Single Number
- [ ] 191 Number of 1 Bits
- [ ] 338 Counting Bits
- [ ] 268 Missing Number
- [ ] Probability: timed mixed puzzle set
- [ ] ML code: re-implement three earlier items, 45 minutes each

### Week 15 — Shortest paths and review

- [ ] 743 Network Delay Time
- [ ] 787 Cheapest Flights Within K Stops
- [ ] 1631 Path With Minimum Effort
- [ ] Redo everything still listed by `python -m dsa due`
- [ ] Mock interviews: one quant-researcher, one MLE
- [ ] Company-tagged LeetCode lists for the firms you are interviewing with

## Two-week sprints

**Quant researcher**
- A timed probability set every day.
- Explain regression and time-series cross-validation without notes.
- Pairs of mediums from weeks 1–8 under a timer.
- One 2–3 hour pandas analysis of a public price dataset, written up like a
  take-home.

**MLE, applied scientist, research scientist**
- About 30 company-tagged LeetCode problems from the last six months (needs
  Premium).
- Re-implement three ML-from-scratch items under a 45-minute timer.
- ML system design.

**Data scientist (modeling)**
- The MLE sprint, with hypothesis testing and regression review in place of
  system design, and an hour of SQL a day.

## Practice method

- Before coding: restate the problem, write examples including edge cases, and
  state the brute force and its complexity.
- Budget 25 minutes for a medium and 40 for a hard. At the budget, read the
  solution, close it, and re-implement it from a blank file.
- Every solution gets a test: the examples, edge cases, and a randomized
  comparison against a brute force (`dsa.stress`).
- Log every attempt with `python -m dsa log`. `python -m dsa due` lists the
  problems to redo, 3, 7 and 21 days after a miss.
- From week 6, one timed mock a week: two mediums in 45–60 minutes, out loud.

## Resources

- LeetCode: neetcode.io (explanations for most problems above);
  *Elements of Programming Interviews in Python*.
- Probability: Zhou, *A Practical Guide to Quantitative Finance Interviews*;
  Crack, *Heard on the Street*; Mosteller, *Fifty Challenging Problems in
  Probability*.
- Statistics and time series: López de Prado, *Advances in Financial Machine
  Learning*, for cross-validation on financial data.
- SQL: LeetCode SQL 50.
- ML code: deep-ml.com; Karpathy's micrograd and minbpe.
- ML system design: Huyen, *Designing Machine Learning Systems*.
