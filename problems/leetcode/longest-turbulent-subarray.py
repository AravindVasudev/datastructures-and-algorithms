# https://leetcode.com/problems/longest-turbulent-subarray/
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        count = 1
        maxCount = 1
        direction = 1 if arr[0] > arr[1] else -1
        
        for i in range(len(arr) - 1):
            if (direction * arr[i]) > (direction * arr[i + 1]):
                count += 1
                direction *= -1
            else:
                maxCount = max(maxCount, count)
                count = 2 if arr[i] != arr[i + 1] else 1
                direction = -1 if arr[i] > arr[i + 1] else 1
                
        return max(maxCount, count)
