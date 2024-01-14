# https://leetcode.com/problems/buildings-with-an-ocean-view/
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        maxRight = 0

        for i in reversed(range(len(heights))):
            if maxRight < heights[i]:
                buildings.append(i)
                maxRight = heights[i]

        return reversed(buildings)
