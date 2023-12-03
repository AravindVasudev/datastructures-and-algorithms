# https://leetcode.com/problems/minimum-time-visiting-all-points/
"""
Prereq:
=======
- Given N points.
- Move: horizontal or vertical or diagnal -> 1 sec/move.
- Visit points in the same order as in the arr.
- Ret time.

Brute Force (Simulation):
=========================
- For each point, find chessboard dist from prev point.
- Add to total.

TC: O(N), where N = len(points).
SC: O(1).
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        offset = lambda x, y: max(abs(y[0] - x[0]), abs(y[1] - x[1]))

        return sum(
            offset(points[i], points[i - 1])
            for i in range(1, len(points)))
