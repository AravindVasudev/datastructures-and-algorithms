# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Reference: https://www.youtube.com/watch?v=LPFhl65R7ww
# The solution basically divides each array into two halves such that left halves of both arrays much contain elements < right halves.
# For this, we pick the smallest array and binary search for this dividing point.
# Start with binary searching through nums1. If mid value of num1 would be its division for the left half.
# For the right half, since we are trying to have two equal sized arrays, subtract the nums1 mid from the mid value of the total array length.
# This way, we get two dividing lines, one for each array. These lines ensure that the total number of elements in the both the left halves combined is
# the same or at max one greater than the right half. Get the first left half end, first right half begining, second left half end, and second right half begining.
# For cases where the divider is at 0 or len(arr), use max values.
# Now, if left1 <= right2 and left2 <= right1, it means the left set contains only elements smaller than right set. This is because both the arrs were sorted initially.
# Then, if the total length is even, then the median is max(left half) + min(right half) / 2. If odd, mac(left half).
# If not, then update the search space -- if left1 > right2 then left is heavy so move right pointer to nums1 mid - 1 else nums1 mid + 1.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total = len(nums1) + len(nums2)
        mid = (total + 1) // 2 # +1 to ensure the mid is ceil
        
        low, high = 0, len(nums1)
        while low <= high:
            nums1Divider = (low + high) // 2
            nums2Divider = mid - nums1Divider
            
            left1 = float("-inf") if nums1Divider == 0 else nums1[nums1Divider - 1]
            right1 = float("inf") if nums1Divider == len(nums1) else nums1[nums1Divider]
            
            left2 = float("-inf") if nums2Divider == 0 else nums2[nums2Divider - 1]
            right2 = float("inf") if nums2Divider == len(nums2) else nums2[nums2Divider]
            
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            
            if left1 > right2:
                high = nums1Divider - 1
            else:
                low = nums1Divider + 1
                
        raise Exception("Invalid Input")
