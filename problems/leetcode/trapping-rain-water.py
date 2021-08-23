# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        leftMax, rightMax = [height[0]], [height[-1]]
        
        for i in range(1, N):
            leftMax.append(max(leftMax[i - 1], height[i]))
            rightMax.append(max(rightMax[i - 1], height[N - i - 1]))
            
        rightMax.reverse()
        
        result = 0
        for i, h in enumerate(height):
            result += min(leftMax[i], rightMax[i]) - h
            
        return result
