# https://leetcode.com/problems/paint-fence/
# https://www.lintcode.com/problem/paint-fence/description
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        if n < 2:
            return n * k

        same, different = k, k * (k - 1)
        for i in range(n - 2):
            same, different = different, (same + different) * (k - 1)

        return same + different