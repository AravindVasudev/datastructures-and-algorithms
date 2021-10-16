# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            if results[-1][1] < intervals[i][0]:
                results.append(intervals[i])
            else:
                results[-1][1] = max(intervals[i][1], results[-1][1])
                
        return results
