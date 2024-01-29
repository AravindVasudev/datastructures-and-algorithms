# https://leetcode.com/problems/non-overlapping-intervals/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sorting by the end time orders the intervals
        # from oldest ending to newest.
        intervals.sort(key=lambda x: x[1])
        overlaps = 0

        # `end` keeps track of the oldest ending time.
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # If the current interval starts after the oldest ending time,
            # given the intervals are ordered by the ending time,
            # we know that the current oldest ending interval
            # doesn't overlap with the previous oldest interval.
            # So, we can update the end to max(end, intervals[i].end).
            # However, given they don't overlap, we can just set end to
            # intervals[i].end.
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                # On overlap, the current overlap starts before the previous
                # oldest interval. Given the intervals are sorted, end is
                # already the largest end time. Just increment overlap count.
                overlaps += 1

        return overlaps
