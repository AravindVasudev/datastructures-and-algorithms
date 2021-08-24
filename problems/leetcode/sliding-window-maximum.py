# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()
        
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1: # out of window
                dq.popleft()
                
            while dq and nums[dq[-1]] < nums[i]:  # remove impossible candidate
                dq.pop()
                
            dq.append(i)
                
            if i >= k - 1:
                result.append(nums[dq[0]])
            
        return result
