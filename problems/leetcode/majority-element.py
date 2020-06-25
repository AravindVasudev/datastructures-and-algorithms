# https://leetcode.com/problems/majority-element/
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurenceMap = defaultdict(int)
        for num in nums:
            occurenceMap[num] += 1
            
        curMax, curMaxCount = -1, 0
        for k, v in occurenceMap.items():
            if v > curMaxCount:
                curMax, curMaxCount = k, v
                
        return curMax
