# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        pqueue = []
        for element, count in counter.items():
            heapq.heappush(pqueue, (count, element))
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)
                
        return [element for _, element in pqueue]
