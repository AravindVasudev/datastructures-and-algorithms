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
