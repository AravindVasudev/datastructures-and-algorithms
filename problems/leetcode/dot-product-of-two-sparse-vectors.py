# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nums[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for i, num in self.nums.items():
            product += num * vec.nums.get(i, 0)

        return product
