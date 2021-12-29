# https://leetcode.com/problems/degree-of-an-array/
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)
        numsDegree = numsCounter.most_common(1)[0][1]
        
        left = 0
        window = Counter()
        minWindowSize = float('inf')
        
        for right, num in enumerate(nums):
            window[num] += 1
            currentDegree = window.most_common(1)[0][1]
            
            while currentDegree == numsDegree:
                minWindowSize = min(minWindowSize, right - left + 1)
                
                window[nums[left]] -= 1
                currentDegree = window.most_common(1)[0][1]
                left += 1
                
        return minWindowSize
