# https://leetcode.com/problems/freedom-trail/
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ringPositions = defaultdict(list)
        for i, char in enumerate(ring):
            ringPositions[char].append(i)

        @cache
        def minSteps(r: int = 0, k: int = 0) -> int:
            if k == len(key):
                return 0

            steps = float("inf")
            for pos in ringPositions[key[k]]:
                diff = abs(r - pos)
                rotation = min(diff, len(ring) - diff)

                steps = min(
                    steps,
                    minSteps(pos, k + 1) + rotation + 1
                )

            return steps

        return minSteps()
