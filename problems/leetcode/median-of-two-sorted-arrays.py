# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        
        nums1Index, nums2Index = 0, 0
        nums1Length, nums2Length = len(nums1), len(nums2)

        while nums1Index < nums1Length and nums2Index < nums2Length:
            if nums1[nums1Index] < nums2[nums2Index]:
                nums.append(nums1[nums1Index])
                nums1Index += 1
            else:
                nums.append(nums2[nums2Index])
                nums2Index += 1
                
        while nums1Index < nums1Length:
            nums.append(nums1[nums1Index])
            nums1Index += 1
            
        while nums2Index < nums2Length:
            nums.append(nums2[nums2Index])
            nums2Index += 1
            
        return nums[len(nums) // 2] * 0.5 + nums[(len(nums) - 1) // 2] * 0.5
