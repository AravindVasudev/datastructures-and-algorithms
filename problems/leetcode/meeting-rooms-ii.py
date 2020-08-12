# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[0])
        
        minHeap = []
        heapq.heappush(minHeap, intervals[0][1])
        
        for interval in intervals[1:]:
            if minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
                
            heapq.heappush(minHeap, interval[1])
            
        return len(minHeap)
