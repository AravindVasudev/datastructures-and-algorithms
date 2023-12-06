# https://leetcode.com/problems/find-the-difference-of-two-arrays/
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
      nums1Set, nums2Set = set(nums1), set(nums2)
      return [list(nums1Set - nums2Set), list(nums2Set - nums1Set)]
