# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # return Counter(arr).most_common(1)[0][0]
        N = len(arr)
        candidates = [arr[N // 4], arr[N // 2], arr[3 * N // 4]]
        target = N / 4

        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate

        return -1
