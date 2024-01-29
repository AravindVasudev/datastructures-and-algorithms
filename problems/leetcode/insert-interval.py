# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # bisect.insort_left(intervals, newInterval)
        self.insort(intervals, newInterval)

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged

    def insort(self, intervals: List[List[int]], newInterval: List[int]) -> None:
        l, r = 0, len(intervals)
        while l < r:
            mid = (l + r) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else:
                r = mid

        intervals.insert(l, newInterval)
