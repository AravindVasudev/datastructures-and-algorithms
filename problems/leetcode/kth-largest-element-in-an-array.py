# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = []
        
        for x in nums:
            heapq.heappush(pqueue, x)
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)
                
        return heapq.heappop(pqueue)
