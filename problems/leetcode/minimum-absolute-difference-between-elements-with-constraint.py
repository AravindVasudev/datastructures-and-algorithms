# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # Sort all the nums.
        nums = sorted((val, idx) for idx, val in enumerate(nums))
        leftHeap, rightHeap = [], []
        diff = float("inf")

        for val, idx in nums:
            # Now that the numbers are ordered, we only have
            # to worry about the indices. leftHeap holds
            # indices min to max, and rightHeap vice-versa.
            heapq.heappush(leftHeap, (idx, val))
            heapq.heappush(rightHeap, (-idx, val))

            # While the smallest index in leftHeap <= idx - x
            # compute diff. We aleady know this is the best
            # possible offset since the original numbers are
            # sorted and every number within the heaps are
            # smaller than the current val.
            while leftHeap and leftHeap[0][0] <= idx - x:
                diff = min(diff, val - heapq.heappop(leftHeap)[1])

            # While the largest index in rightHeap >= idx + x.
            while rightHeap and -rightHeap[0][0] >= idx + x :
                diff = min(diff, val - heapq.heappop(rightHeap)[1])

        return diff
