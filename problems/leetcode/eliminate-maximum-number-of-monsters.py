# https://leetcode.com/problems/eliminate-maximum-number-of-monsters
"""
Prereq:
=======
1. Fighting `n` monsters.
2. arr `dist` contains initial distance of the ith monster.
3. Monsters walk at constant speed.
4. arr `speed` contains speed of the ith monster.
5. Weapon can elimate one monster every charge (a minute).
6. Weapon starts charged.
7. Lose when monster reaches the city.
8. If monster reaches when the weapon is charged, still lose.
9. Ret max num of monster you can defeat.

Observations:
=============
- Each monster moves by dist - speed at each turn.
- Ideally we have to destroy the monster that would reach first to maximize.
    - steps = int(dist / speed)
    - Pick the one with least # of steps.

Brute Force:
============
1. score = 0
2. while score < n:
    2.1. foreach monster:
        2.1.1. steps = int(dist / speed)
        2.1.2. Find min step monster.
        2.1.3. if steps <= 0: ret score.
    2.2. Destroy the monster (set tombstone in the arr).
    2.3. score++
    2.4. Update dist.
3. ret score.

TC: O(N^2)
SC: O(1)

Observations:
=============
- All that matters is the # of steps.
    - Dist & Speed --> number of steps.
- We need to deal with monsters from closest to farthest.
    - a.k.a non-decreasing order.

Optimization I:
===============
1. Foreach monster: # O(N)
    1.1. Compute steps array.
2. sort(steps) # O(N log N)
3. foreach steps: # O(N)
    3.1. steps <= index:
        3.1.1. ret len(steps[:index])
4. ret len(monster)

TC: O(N log N), where N = number of monsters
SC: O(N) for steps array.

Optimization II:
===============
- Bucket Sort (TBD).
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Compute steps array.
        steps = [d/s for d, s in zip(dist, speed)]

        # Sort steps in non-decreasing order.
        steps.sort()

        # Calculate # of monsters killed.
        for i, step in enumerate(steps):
            if step <= i:
                return i

        # All the monsters all been killed.
        return len(dist)
