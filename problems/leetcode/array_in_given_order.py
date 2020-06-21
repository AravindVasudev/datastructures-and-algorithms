# https://leetcode.com/problems/create-target-array-in-the-given-order/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            pos = index[i]
            size = len(target)
            prev, cur = nums[i], None
            while (pos < size) and target[pos] != -1:
                cur = target[pos]
                target[pos] = prev

                prev = cur
                pos += 1

            target[pos] = prev

                
        return target
