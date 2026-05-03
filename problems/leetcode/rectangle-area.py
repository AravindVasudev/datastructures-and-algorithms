"""

(-3, 0) - (3, 4) # (ax2 - ax1) * (ay2 - ay1)

x-axis
# https://leetcode.com/problems/rectangle-area/
=======
-3 -2 -1 0 1 2 3 
3 - (-3) = 6 # (ax2 - ax1)

y-axis
=======
0 1 2 3 4
4 - 0 = 4 # (ay2 - ay1)

(0, -1) - (9, 2) # (bx2 - bx1) * (by2 - by1)

Overlap
========
rectA's width goes from ax1 ---- ax2
rectB's width goes from bx1 ---- bx2

 |--------------------------|
ax1                        ax2
                   |-------------------------|
                   bx1                      bx2

- min(ax2, bx2) is the end of the overlap line segment.
- max(ax1, bx1) is the beginning of the overlap line segment.

So, length = min(ax2, bx2) - max(ax1, bx1)

When there is no overlap, length < 0.

 |--------------------------|      |---------------------|
ax1                        ax2     bx1                   bx2

length = min(ax2, bx2) - max(ax1, bx1) = ax2 - bx1 < 0.
"""

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Helper fns.
        area = lambda x1, y1, x2, y2: (x2 - x1) * (y2 - y1) # Area of a rectangle.
        overlap = lambda x1, x2, y1, y2: min(x2, y2) - max(x1, y1) # Overlap length of two line segments.

        # Find total area.
        rectAArea = area(ax1, ay1, ax2, ay2)
        rectBArea = area(bx1, by1, bx2, by2)

        # Find overlap area.
        overlapWidth = overlap(ax1, ax2, bx1, bx2)
        overlapHeight = overlap(ay1, ay2, by1, by2)

        overlapArea = 0
        if overlapWidth > 0 and overlapHeight > 0:
            overlapArea = overlapWidth * overlapHeight

        return rectAArea + rectBArea - overlapArea
