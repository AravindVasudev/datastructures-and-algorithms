# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        priorityQueue = []
        
        for num in arr:
            heapq.heappush(priorityQueue, (abs(x - num), num))
            
        output = []
        for _ in range(k):
            output.append(heapq.heappop(priorityQueue)[1])
            
        output.sort()
        return output
