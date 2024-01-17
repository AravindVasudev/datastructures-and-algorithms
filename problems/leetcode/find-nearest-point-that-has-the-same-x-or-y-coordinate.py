# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan = lambda point: abs(x - point[0]) + abs(y - point[1])

        index, smallest = -1, float("inf")
        for i, point in enumerate(points):
            if not (point[0] == x or point[1] == y):
                continue

            distance = manhattan(point)
            if distance < smallest:
                index, smallest = i, distance

        return index
