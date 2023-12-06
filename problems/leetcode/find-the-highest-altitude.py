# https://leetcode.com/problems/find-the-highest-altitude/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAltitude = 0

        for g in gain:
            altitude += g
            maxAltitude = max(maxAltitude, altitude)

        return maxAltitude
