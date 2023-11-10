    def leftRightDifference(self, nums: List[int]) -> List[int]:
        

        leftSum = [0] * len(nums)
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        rightSum = [0] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = abs(leftSum[i] - rightSum[i])

        return result
