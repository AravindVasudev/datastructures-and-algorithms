# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums):
        permutations = []
        for i, num in enumerate(nums):
            if num == '#':
                continue

            nums[i] = '#'
            for permutation in self.permute(nums):
                permutations.append([num] + permutation)
                
            nums[i] = num
            
        return permutations if permutation else [[]]

# Alternative swap solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == len(nums):
                result.append(list(nums))
            
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        result = []
        backtrack()
        return result
                
