# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N = len(potions)
        potions.sort()
        result = []
        for spell in spells:
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r) // 2
                strength = spell * potions[mid]
                if strength < success:
                    l = mid + 1
                else:
                    r = mid - 1

            result.append(N - l)


        return result
