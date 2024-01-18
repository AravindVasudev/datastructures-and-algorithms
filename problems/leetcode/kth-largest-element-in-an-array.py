# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = []
        
        for x in nums:
            heapq.heappush(pqueue, x)
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)
                
        return heapq.heappop(pqueue)

# Quick-Select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        pivot = random.choice(nums) # Pick a random pivot.

        # Partition in descending order.
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        # Pick which half to look for.
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - (L + M))
        else:
            return mid[0]
