# https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = lambda x, y: [max(x[0], y[0]), min(x[1], y[1])]

        intersections = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            inter = intersection(firstList[i], secondList[j])
            if inter[0] <= inter[1]:
                intersections.append(inter)

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
