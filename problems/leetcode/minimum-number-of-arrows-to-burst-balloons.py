# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                arrows += 1

        return arrows
