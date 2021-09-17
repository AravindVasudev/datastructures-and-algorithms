# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        nums1Count = Counter(nums1)
        nums2Count = Counter(nums2)
            
        if len(nums1Count) > len(nums2Count):
            nums1Count, nums2Count = nums2Count, nums1Count
            
        for k, v in nums1Count.items():
            result += [k] * min(v, nums2Count[k])
            
        return result
