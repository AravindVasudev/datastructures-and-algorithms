# https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
Breakdown:
==========
- Given: list of heights.
- Each bar has height = heights[i] & width = 1.
- area = min(heights[i:j]) * (j - i + 1) for the range [i, j).
- Return: max(area).

Brute Force:
============
- If we know the minimum height for every range, we can calculate area.

[2,1,5,6,2,3]

      *
    * *
    * *   *
    * * * *
*   * * * *
* * * * * *

fn largestRectangleArea(heights) -> max(area):
    1. N = len(heights)
    2. foreach i in [0, N)
        2.1. minHeight = heights[i]
        2.2. foreach j in (i, N)
            2.2.1. minHeight = min(minHeight, heights[j])
            2.2.2. width = j - i + 1
            2.2.3. largest = max(largest, minHeight * width)
    3. return largest

TC: O(N^2), where N = len(heights).
SC: O(1).

Analysis:
=========
- The above approach takes O(N^2) because we are looking at every possible range.
- We can note that a rectangle ends when the next histogram bar is smaller than the current.
    - Because only min(heights[i:j]) matter.
- If we can maintain a stack with height and starting position of rectangle, we can update max(area) when
  we encounter a smaller bar.

Approach II: stacks:
====================
fn largestRectangleArea(heights) -> max(area):
    1. N = len(heights)
    2. foreach i in [0, N) #O(N)
        2.1. while stack & heights[stack[-1]] > heights[i]:
            2.1.1. h = stack.pop()
            2.1.2. w = i - stack[-1] - 1
            2.1.3. largest = max(largest, h * w)
    3. while stack
        3.1. h = stack.pop()
        3.2. N - stack[-1] - 1
        3.3. largest = max(largest, h * w)
    4. return largest

TC: O(N), where N = len(heights).
SC: O(N), for the stack.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        largest = 0
        stack = []

        def popAndUpdate(i):
            nonlocal largest
            h = heights[stack.pop()]
            w = (i - stack[-1] - 1) if stack else i

            largest = max(largest, h * w)

        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                popAndUpdate(i)

            stack.append(i)

        while stack:
            popAndUpdate(N)

        return largest
