class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxKid = max(candies)
        return [x+extraCandies >= maxKid for x in candies]
