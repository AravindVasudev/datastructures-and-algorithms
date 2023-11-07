"""
Prereq:
=======
1. wooden plank length = n
2. ant moves 1 unit/sec.
3. ants can move left or right.
4. when opposite ants meet, they change direction.
5. Changing direction time = 0.
6. When ant reaches end, it falls.

Brute Force (Simulation):
=========================
1. while true:
    1.0. time++
    1.1. Move all ants by one index.
    1.2. If any left and right ant meet: no-op
    1.3. if ant < 0 or ant > n: set tombstone.
    1.4. if all ants fall, return time.

TC: O(N * M), N = length of the plank, M = total # of ants
SC: O(1)

Observations:
=============
- "when opposite ants meet, they change direction" is a no-op.
    - ants currently do not have any spoecial property like speed so them changing direction is literally same as having them in the same direction.
- Each ant moves one step at a time.
- And we only need to find the time taken by the slowest ant.
- Given all ants move in the same speed, slowest == farthest.
- # of steps for an ant = N - position.

Optimization (Computation):
===========================
1. fartest = 0
2. Foreach ant in left:
    2.1. fartest = max(fartest, N - index)
3. Foreach ant in right:
    3.1. fartest = max(fartest, index)
4. ret fartest

TC: O(M), M = total # of ants.
SC: O(1)
"""

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not (left or right):
            return 0

        if not right:
            return max(left)

        if not left:
            return n - min(right)

        return max(n - min(right), max(left))
