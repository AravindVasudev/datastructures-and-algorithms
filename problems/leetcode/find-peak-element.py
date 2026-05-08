# https://leetcode.com/problems/find-peak-element/
"""
1 2 3 1
    |

1 2 1 3 5 6 4
  |       |
  1       5



    3
  2     1
1       

                6
             5
                    4
        3 
  2
1    1
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid

        return start
