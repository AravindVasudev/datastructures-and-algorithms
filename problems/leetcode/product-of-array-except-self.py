# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        leftProducts = [1] * N
        rightProducts = [1] * N
        result = [1] * N
        
        # Add all left products
        for i in range(1, N):
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1]
        
        # Add all right products
        for i in range(N - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]
        
        # Compute results
        for i in range(N):
            result[i] = leftProducts[i] * rightProducts[i]
            
        return result
