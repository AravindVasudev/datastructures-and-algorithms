# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        pairs = 0

        for num in nums:
          diff = k - num
          if diff == num and count[num] < 2:
            continue

          if count[diff] and count[num]:
            count[diff] -= 1
            count[num] -= 1
            pairs += 1

        return pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        pairs = 0

        while l < r:
          if nums[l] + nums[r] == k:
            pairs += 1
            r -= 1
            l += 1
          elif nums[l] + nums[r] > k:
            r -= 1
          else:
            l += 1

        return pairs
