# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        low, high, mid = 0, len(nums1), (len(nums1) + len(nums2) + 1) // 2
        while low <= high:
            part1 = (low + high) // 2
            part2 = mid - part1
            
            left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            right1 = float('inf') if part1 == len(nums1) else nums1[part1]
            
            left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            right2 = float('inf') if part2 == len(nums2) else nums2[part2]
            
            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
                
            if left1 > right2:
                high = part1 - 1
            else:
                low = part1 + 1
                
        return -1
