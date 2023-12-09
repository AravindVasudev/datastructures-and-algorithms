# https://leetcode.com/problems/maximum-subsequence-score/
"""
At initial glance, this looks like a backtracking problem. And yes, this can be solved using backtracking:

```
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        score = lambda x: sum(nums1[i] for i in x) * min(nums2[i] for i in x)

        def compute(index, path):
            if len(path) == k:
                print(path, score(path))
                return score(path)

            if index == len(nums1):
                return 0

            return max(compute(index + 1, path),
                       compute(index + 1, path + [index]))

        return compute(0, [])
```

However, this above solution TLEs because it takes about O(nCk), where n = len(nums1). This is because this literally generates every k element combination of indexes. We can do much better.

We have to notice two things from the question that will help us avoid generating nCk combinations of indices:
1. Even though the question explicitly specifies "subsequence", we don't need to generate an actual "subsequence". We are concerned with the sum(subsequence) and addition is commutative. As in, the order doesn't matter. This boils down the question from generating nCk combinations to simply picking k indices.

2. Even though we are asked to select "minimum" element in nums2, we are still trying to maximize it. As in, since we are trying to find maximum score, and min(nums2) is multiplied with the score, we want to pick indices where nums2 is maximum.

With these two clarifications, the problem can be simplified as follows:
- Since we are picking same indices in both arrays, combine them as pairs.
- Sort the combined array in descending order of nums2. When we pick a pair in order from this array, we know we are picking the best possible nums2 this way.
- pick a pair and add to the total. We don't have to worry about finding min(nums2) since the current picked element from nums2 is the minimum in the current total set. (because it is sorted by nums2).
- Now the remaining problem is simplified: we just have to pick k max nums1. This is a standard heap problem.
    - Add n1 to heap.
    - if len(heap) > k then remove the smallest (remember, we don't have to adjust n2 since the current n2 is the smallest possbile n2 since the pairs are sorted).
    - if len(heap) == k then update score.
- return max score.

TC: O(N log N)
SC: O(N)
"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(list(zip(nums1, nums2)), key=lambda x: -x[1])
        total, score = 0, 0
        pq = []

        for n1, n2 in pairs:
            total += n1
            heapq.heappush(pq, n1)

            if len(pq) > k:
                total -= heapq.heappop(pq)

            if len(pq) == k:
                score = max(score, total * n2)

        return score
