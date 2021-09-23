# https://leetcode.com/problems/k-closest-points-to-origin/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Straight-forward solution O(N log N)
        # return sorted(points, key=lambda x: x[0]**2+x[1]**2)[:k]
        
        pqueue = []
        for x in points:
            # Max heap for euclidean distance
            heapq.heappush(pqueue, (-(x[0]**2 + x[1]**2), x))
            
            if len(pqueue) > k:
                heapq.heappop(pqueue)
                
        return [point[1] for point in pqueue]
