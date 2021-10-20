# https://leetcode.com/problems/sliding-window-median/
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or len(nums) < 1 or k < 1 or k > len(nums):
            return []
        
        lo = [] # Max Heap
        hi = [] # Min Heap

        # Init starting window
        for i in range(k):
            if len(lo) == len(hi):
                heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
            else:
                heapq.heappush(hi, -heapq.heappushpop(lo, -nums[i]))
        
        toRemove = defaultdict(int) # Add indices for lazy removal
        result = [float(-lo[0])] if k & 1 else [(-lo[0] + hi[0]) / 2]
        
        
        for i in range(k, len(nums)):
            # Add to lo
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
            
            outNum = nums[i - k] # Num to remove
            toRemove[outNum] += 1
                
            # If outNum falls within hi, balance by moving one num
            # from lo to hi. Balancing ensures the heap tops are valid.
            if outNum > -lo[0]:
                heapq.heappush(hi, -heapq.heappop(lo))
            
            # Lazy remove from lo
            while lo and toRemove[-lo[0]]:
                toRemove[-lo[0]] -= 1
                heapq.heappop(lo)
                
            # Lazy remove from hi
            while hi and toRemove[hi[0]]:
                toRemove[hi[0]] -= 1
                heapq.heappop(hi)
                
            # Calculate median
            result.append(float(-lo[0]) if k & 1 else (-lo[0] + hi[0]) / 2)
                
        return result
