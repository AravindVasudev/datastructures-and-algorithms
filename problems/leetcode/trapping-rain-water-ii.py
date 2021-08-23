# https://leetcode.com/problems/trapping-rain-water-ii/
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        pqueue = []
        visited = [[False] * N for _ in range(M)]
        
        # Add all the boundary to a priority queue
        for i in range(M):
            visited[i][0] = visited[i][N - 1] = True
            heapq.heappush(pqueue, (heightMap[i][0], i, 0))
            heapq.heappush(pqueue, (heightMap[i][N - 1], i, N - 1))
            
        for j in range(N):
            visited[0][j] = visited[M - 1][j] = True
            heapq.heappush(pqueue, (heightMap[0][j], 0, j))
            heapq.heappush(pqueue, (heightMap[M - 1][j], M - 1, j))
            
        result = 0
        while pqueue:
            height, i, j = heapq.heappop(pqueue) # pick a cell
            
            # Check the neighbors to see if this see blocks any water
            # for them. This means, this cell's height should be
            # more than the neighbor. So basically if it is, add
            # the difference to result and add the neighbor to the
            # priority queue. For the neighbor's height use the max of
            # current cell and its height because whichever is taller
            # will serve as the wall to hold water.
            for directionI, directionJ in directions:
                nextI, nextJ = i + directionI, j + directionJ
                if 0 <= nextI < M and 0 <= nextJ < N and not visited[nextI][nextJ]:
                    result += max(0, height - heightMap[nextI][nextJ]) # add 
                    heapq.heappush(pqueue, (max(height, heightMap[nextI][nextJ]), nextI, nextJ))
                    visited[nextI][nextJ] = True
                    
        return result
