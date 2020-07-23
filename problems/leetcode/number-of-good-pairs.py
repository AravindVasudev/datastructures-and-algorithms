# https://leetcode.com/problems/number-of-good-pairs/
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)
            
        total = 0
        for numCount in count.values():
            size = len(numCount)
            total += (size * (size - 1)) // 2
            
        return total
